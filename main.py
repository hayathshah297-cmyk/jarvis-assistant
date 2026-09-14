import os
import google.generativeai as genai

# Gemini AI सेटअप
API_KEY = os.getenv("GEMINI_API_KEY")
if API_KEY:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")

def jarvis_respond(user_input):
    if not API_KEY:
        return "कृपया अपनी Gemini API Key सेट करें।"
    
    prompt = f"आप एक जार्विस की तरह AI असिस्टेंट हैं। यूजर के इस सवाल का समझदारी से और संक्षिप्त जवाब दें: {user_input}"
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    print("Jarvis System Active...")
    print(jarvis_respond("नमस्ते जार्विस, तुम क्या कर सकते हो?"))
  
