from tools.google.gmail_tools import GmailTool
import os

def main():
    # Path to the client secret file
    work_dir = os.path.dirname(__file__)
    client_secret_path = os.path.join(work_dir, 'client-secret.json')
    gmail = GmailTool(client_secret_path)
    result = gmail.send_email(
        to='tejasrokade@gmail.com',
        subject='Test Email from MCP Gmail',
        body='Hello, this is a test email sent from MCP Gmail project!',
    )
    print(result)

if __name__ == "__main__":
    main()


# Original code to run for the claude DeskTop(ONly in MacOS and Windows)
# def main():
 #   print("Hello from mcp-gmail!")


#if __name__ == "__main__":
  #  main()
