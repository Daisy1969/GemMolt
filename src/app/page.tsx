'use client';

import React, { useEffect, useState } from 'react';
import AIChat from '../components/AIChat';
import ThemeToggle from '../components/ThemeToggle';

export default function Home() {
    const [os, setOs] = useState<'Windows' | 'Mac' | 'Linux' | 'Unknown'>('Unknown');

    useEffect(() => {
        const userAgent = window.navigator.userAgent;
        if (userAgent.indexOf('Win') !== -1) setOs('Windows');
        else if (userAgent.indexOf('Mac') !== -1) setOs('Mac');
        else if (userAgent.indexOf('Linux') !== -1) setOs('Linux');
    }, []);

    const getDownloadLink = () => {
        if (os === 'Windows') return '/scripts/install_openclaw.bat';
        if (os === 'Mac' || os === 'Linux') return '/scripts/mac_install.sh';
        return '#';
    };

    const getButtonText = () => {
        if (os === 'Windows') return 'Download Installer for Windows';
        if (os === 'Mac') return 'Download Installer for Mac';
        if (os === 'Linux') return 'Download Installer for Linux';
        return 'Download Installer';
    };

    return (
        <main className="min-h-screen bg-gray-50 dark:bg-gray-900 flex flex-col font-sans text-gray-900 dark:text-gray-100 transition-colors duration-300">

            {/* Header / Hero */}
            <header className="bg-white dark:bg-gray-800 shadow-sm p-6 text-center transition-colors duration-300">
                <h1 className="text-4xl font-extrabold text-blue-700 dark:text-blue-400 tracking-tight">OpenClaw Setup</h1>
                <p className="mt-2 text-xl text-gray-600 dark:text-gray-300">Simple, secure installation for your computer.</p>
            </header>

            {/* Theme Toggle */}
            <ThemeToggle />

            {/* Main Content */}
            <div className="flex-1 flex flex-col items-center justify-center p-8 text-center max-w-4xl mx-auto space-y-12 z-10">

                {/* Welcome Text */}
                <div className="space-y-4">
                    <h2 className="text-3xl font-bold dark:text-gray-100">Welcome!</h2>
                    <p className="text-xl text-gray-700 dark:text-gray-300 leading-relaxed max-w-2xl">
                        We are here to help you get started with OpenClaw. This tool will help your computer work better for you.
                        You don't need to be a computer expert.
                    </p>
                </div>

                {/* Dynamic Installer Section */}
                <div className="bg-white dark:bg-gray-800 p-10 rounded-3xl shadow-xl border-2 border-blue-100 dark:border-gray-700 w-full max-w-lg transition-transform hover:scale-105">
                    {os === 'Unknown' ? (
                        <p className="text-lg text-gray-500 dark:text-gray-400 animate-pulse">Detecting your computer type...</p>
                    ) : (
                        <div className="space-y-6">
                            <div className="flex justify-center text-6xl mb-4">
                                {os === 'Windows' ? '🪟' : os === 'Mac' ? '🍎' : '🐧'}
                            </div>
                            <h3 className="text-2xl font-bold text-gray-800 dark:text-white">We detected you are on {os}</h3>
                            <p className="text-gray-600 dark:text-gray-300">
                                Click the button below to download the automatic setup helper.
                            </p>

                            <a
                                href={getDownloadLink()}
                                download
                                className="block w-full py-4 bg-blue-600 hover:bg-blue-700 text-white text-xl font-bold rounded-xl shadow-md transition-all transform active:scale-95"
                            >
                                {getButtonText()}
                            </a>

                            <div className="text-sm text-gray-500 dark:text-gray-400 mt-4 bg-yellow-50 dark:bg-yellow-900/20 p-3 rounded-lg border border-yellow-100 dark:border-yellow-800/30">
                                <strong>Start Instructions:</strong><br />
                                1. Click Download<br />
                                2. Open the file
                                {os === 'Windows' ? ' (Check your Downloads folder)' : ' (You may need to run it in Terminal)'}
                            </div>
                        </div>
                    )}
                </div>

                {/* Privacy Note */}
                <div className="text-gray-500 dark:text-gray-400 text-sm max-w-lg">
                    <p>
                        🔒 <strong>Privacy First:</strong> This website and the assistant below do not save your personal data.
                        Everything disappears when you close this window.
                    </p>
                </div>

                {/* Version Footer */}
                <footer className="text-gray-400 dark:text-gray-600 text-xs mt-8">
                    v1.0.0
                </footer>

            </div>

            {/* Chat Widget */}
            <AIChat />

        </main>
    );
}
