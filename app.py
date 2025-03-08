from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    title = "My Flask Blog"
    
    # List of blog posts (each post is a dictionary)
    blog_posts = [
        {"title": "My First Blog Post", "author": "Sierra", "content": "This is my first post using Flask!", "date": "March 5, 2025"},
        {"title": "Learning Python", "author": "Sierra", "content": "Today, I learned about Flask and templates!", "date": "March 6, 2025"},
        {"title": "Why I Love Coding", "author": "Sierra", "content": "Coding lets me create and automate things. It's amazing!", "date": "March 7, 2025"}
    ]

    return render_template("index.html", title=title, blog_posts=blog_posts)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
