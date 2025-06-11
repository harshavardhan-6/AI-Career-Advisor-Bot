# AI Career Advisor Bot (Basic Version)
def ai_career_advisor():
    print("Welcome to AI Career Advisor Bot!")
    name = input("What's your name? ")
    field = input(f"Hi {name}, what is your area of interest? (e.g., AI, Web Dev, Embedded Systems): ").lower()

    if field in ["ai", "artificial intelligence", "machine learning", "ml", "data science"]:
        print("\nCareer Advice for AI:")
        print("- Learn Python, NumPy, pandas, and scikit-learn.")
        print("- Explore deep learning using TensorFlow or PyTorch.")
        print("- Projects: AI chatbots, recommender systems, computer vision apps.")
        print("- Join GitHub repos like: https://github.com/llSourcell/Learn_Machine_Learning")
    
    elif field in ["web", "web development", "frontend", "backend"]:
        print("\nCareer Advice for Web Development:")
        print("- Learn HTML, CSS, JavaScript, React, and Node.js.")
        print("- Full stack knowledge is a bonus (MERN stack).")
        print("- Projects: Portfolio sites, e-commerce apps, REST APIs.")
        print("- GitHub: https://github.com/donnemartin/system-design-primer")
    
    elif field in ["embedded systems", "iot", "arduino", "raspberry pi"]:
        print("\nCareer Advice for Embedded Systems:")
        print("- Learn C/C++, microcontrollers, and real-time OS.")
        print("- Work with Arduino and Raspberry Pi.")
        print("- Projects: Home automation, robotics, IoT apps.")
        print("- GitHub: https://github.com/curiousmotor/awesome-embedded-systems")
    
    else:
        print("\nSorry, I don't have info on that field yet.")
        print("Try fields like: AI, Web Dev, or Embedded Systems.")
    
    print("\nThanks for using the AI Career Advisor Bot!")

if __name__ == "__main__":
    ai_career_advisor()
