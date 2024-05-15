from django.shortcuts import render

context_desc = {
  "index": {
    "sub_head": "I build things for the web.",
    "info": """I'm a software engineer specializing in building(and occasionaly designing). Currently I'm foused in building
    accessible, human centered products in Django.""",
  },

  "about": """Hello! I'm Saurav, a passionate individual with a keen interest in software engineering and technology. I'm currently pursuing a Bachelor's degree in Software Engineering at Pokhara University. My journey in the field of technology began early, fueling my curiosity to explore and innovate. Throughout my academic and personal endeavors, I've developed a strong foundation in Python. I enjoy solving complex problems and turning ideas into functional solutions.
  Aside from my academic pursuits, I actively engage in projects and collaborations to broaden my skills and contribute to meaningful initiatives within the tech community. Whether it's developing software applications or participating in hackathons, I thrive on the excitement of pushing boundaries and creating impactful solutions.
  When I'm not coding, you can find me exploring the latest trends in technology, indulging in a good book, or enjoying outdoor adventures. I believe in continuous learning and strive to embrace every opportunity for personal and professional growth.
  Thank you for taking the time to learn a bit about me. Feel free to explore my portfolio and reach out if you'd like to connect or collaborate!""",

  "skills": {
    "info": "At the heart of my skills lies a skill set, honed through experience",
    "all_skills" : ["Problem Solving", "HTML, CSS", "JavaScript", "Django", "NodeJS with Express", "MYSQL", "Version control from Git & Github", "Docker"]
  },

  "projects": {
    "scheduler": {
      "info": """An android and web based app that lets students get notices from their institutes with ease.
      Build using flutter and firebase""",
    },
    "NepseAPI" : "Access NepseAPI for free in your application.",
  }
}

def index(req):
  context = {
    "index": context_desc["index"]
  }
  return render(req, "index.html", context)

def skills(req):
  context = {
    "skills": context_desc["skills"]
  }
  return render(req, "skills.html", context)

def projects(req):
  return render(req, "projects.html")

def about(req):
  return render(req, "about.html")