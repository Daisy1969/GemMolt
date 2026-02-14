'use client';

import React, { useState, useRef, useEffect } from 'react';

type Message = {
    role: 'user' | 'model';
    content: string;
};

export default function AIChat() {
    const [messages, setMessages] = useState<Message[]>([
        { role: 'model', content: "Hello! I'm ClawBuddy here to help you get OpenClaw set up nicely. What kind of computer are you using today?" }
    ]);
    const [input, setInput] = useState('');
    const [loading, setLoading] = useState(false);
    const [isOpen, setIsOpen] = useState(true);
    const messagesEndRef = useRef<HTMLDivElement>(null);

    const scrollToBottom = () => {
        messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
    };

    useEffect(() => {
        scrollToBottom();
    }, [messages, isOpen]);

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        if (!input.trim() || loading) return;

        const userMessage = input.trim();
        setInput('');
        setLoading(true);

        const newMessages: Message[] = [...messages, { role: 'user', content: userMessage }];
        setMessages(newMessages);

        try {
            const res = await fetch('/api/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ messages: newMessages }),
            });

            if (!res.ok) throw new Error('API failed');

            const data = await res.json();
            setMessages((prev) => [...prev, { role: 'model', content: data.content }]);
        } catch (error) {
            setMessages((prev) => [...prev, { role: 'model', content: "Oh dear, I seem strictly to have lost my train of thought. Could you try asking me again?" }]);
        } finally {
            setLoading(false);
        }
    };

    if (!isOpen) {
        return (
            <button
                onClick={() => setIsOpen(true)}
                className="fixed bottom-4 right-4 bg-blue-600 text-white p-4 rounded-full shadow-lg hover:bg-blue-700 transition-colors z-50 text-xl font-bold"
                aria-label="Open Chat Assistant"
            >
                🦞 Help
            </button>
        );
    }

    return (
        <div className="fixed bottom-4 right-4 w-96 max-w-[90vw] h-[500px] max-h-[80vh] bg-white rounded-xl shadow-2xl flex flex-col border border-gray-200 z-50 overflow-hidden font-sans">
            {/* Header */}
            <div className="bg-blue-600 p-4 text-white flex justify-between items-center shrink-0">
                <div className="flex items-center gap-2">
                    <span className="text-2xl">🦞</span>
                    <div>
                        <h3 className="font-bold text-lg">ClawBuddy</h3>
                        <p className="text-xs opacity-90">Your Setup Assistant</p>
                    </div>
                </div>
                <button
                    onClick={() => setIsOpen(false)}
                    className="text-white/80 hover:text-white text-2xl"
                    aria-label="Minimize Chat"
                >
                    &times;
                </button>
            </div>

            {/* Messages */}
            <div className="flex-1 overflow-y-auto p-4 space-y-4 bg-gray-50">
                {messages.map((msg, idx) => (
                    <div
                        key={idx}
                        className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}
                    >
                        <div
                            className={`max-w-[80%] p-3 rounded-2xl text-sm md:text-base leading-relaxed ${msg.role === 'user'
                                    ? 'bg-blue-600 text-white rounded-tr-none'
                                    : 'bg-white text-gray-800 border border-gray-200 rounded-tl-none shadow-sm'
                                }`}
                        >
                            {msg.content}
                        </div>
                    </div>
                ))}
                {loading && (
                    <div className="flex justify-start">
                        <div className="bg-white p-3 rounded-2xl rounded-tl-none border border-gray-200 shadow-sm text-gray-500 italic text-sm">
                            Thinking...
                        </div>
                    </div>
                )}
                <div ref={messagesEndRef} />
            </div>

            {/* Input */}
            <form onSubmit={handleSubmit} className="p-4 bg-white border-t border-gray-200 shrink-0">
                <div className="flex gap-2">
                    <input
                        type="text"
                        value={input}
                        onChange={(e) => setInput(e.target.value)}
                        placeholder="Type a question..."
                        className="flex-1 border border-gray-300 rounded-full px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 text-gray-700"
                        disabled={loading}
                    />
                    <button
                        type="submit"
                        disabled={loading || !input.trim()}
                        className="bg-blue-600 text-white p-2 rounded-full hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors w-10 h-10 flex items-center justify-center"
                        aria-label="Send Message"
                    >
                        ➤
                    </button>
                </div>
            </form>
        </div>
    );
}
