import { NextResponse } from 'next/server';

const SYSTEM_PROMPT = `
You are ClawBuddy, a helpful, patient, and pleasant AI assistant designed to help older adults (specifically around 90 years old) install and onboard OpenClaw.
Your tone should be warm, encouraging, and respectful. Avoid technical jargon where possible.
You are a master of setup.
The user might be on Windows, Mac, or Linux.
You should guide them to download the correct script from the website if they haven't already.
The website automatically detects their OS and offers a "One Click" installer.
For Windows, it is "install_openclaw.bat".
For Mac/Linux, it is "mac_install.sh".
If they are stuck, explain steps simply.
Do not ask for personal information.
Do not store any user data.
`;

export async function POST(req: Request) {
    try {
        const { messages } = await req.json();
        const apiKey = process.env.GEMINI_API_KEY;

        if (!apiKey) {
            // Fallback or error if no key
            return NextResponse.json({
                role: 'model',
                content: "I'm ready to help, but my brain (API Key) isn't connected yet. Please ask the administrator to configure the GEMINI_API_KEY."
            });
        }

        // Use gemini-1.5-flash for better speed and reliability
        const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${apiKey}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                contents: messages.map((m: any) => ({
                    role: m.role === 'user' ? 'user' : 'model',
                    parts: [{ text: m.content }]
                })),
                systemInstruction: {
                    parts: [{ text: SYSTEM_PROMPT }] // NOTE: System instruction syntax varies by model version, valid for some gemini versions
                }
            })
        });

        const data = await response.json();

        // Handle potential API errors or format differences
        if (!response.ok) {
            console.error("Gemini API Error:", JSON.stringify(data, null, 2));
            return NextResponse.json({ role: 'model', content: "I'm having a little trouble thinking right now. Please try again." });
        }

        const reply = data.candidates?.[0]?.content?.parts?.[0]?.text || "I'm not sure what to say.";

        return NextResponse.json({ role: 'model', content: reply });

    } catch (error) {
        console.error('Error in chat API:', error);
        return NextResponse.json({ error: 'Internal Server Error' }, { status: 500 });
    }
}
