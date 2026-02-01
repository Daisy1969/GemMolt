import sys
import os
from colorama import init, Fore, Style

# Add the src directory to python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.core.orchestrator import Orchestrator
from src.interfaces.message_listener import run_server
import threading


def main():
    init(autoreset=True)
    print(f"{Fore.CYAN}Initializing GemMolt Assistant v0.1...{Style.RESET_ALL}")
    
    try:
        if not os.path.exists(os.path.join(os.path.dirname(__file__), '..', '.env')):
             print(f"{Fore.YELLOW}Warning: .env file not found. Functionality will be limited.{Style.RESET_ALL}")

        bot = Orchestrator()
        
        # Start Message Server in background thread
        print(f"{Fore.YELLOW}Starting iMessage Listener on port 5000...{Style.RESET_ALL}")
        server_thread = threading.Thread(target=run_server, args=(bot,), daemon=True)
        server_thread.start()

        print(f"{Fore.GREEN}System Online. Gemini Connected.{Style.RESET_ALL}")

        print("Type 'exit' to stop.")

        while True:
            user_input = input(f"{Fore.BLUE}You: {Style.RESET_ALL}")
            if user_input.lower() in ['exit', 'quit']:
                break
            
            print(f"{Fore.CYAN}Processing...{Style.RESET_ALL}")
            response = bot.handle_input(user_input)
            print(f"{Fore.MAGENTA}GemMolt: {Style.RESET_ALL}{response}")

    except Exception as e:
        print(f"{Fore.RED}Critical Error: {e}{Style.RESET_ALL}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
