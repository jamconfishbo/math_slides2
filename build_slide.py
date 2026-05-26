import sys
import os
import math
import subprocess

def format_sign(num):
    return "+" if num >= 0 else "-"

def build_slides(a, b, c):
    # --- 1. ALGEBRAIC LOGIC ---
    ac = a * c
    m, n = None, None
    for i in range(-abs(ac) - 1, abs(ac) + 2):
        if i == 0: continue
        if ac % i == 0:
            j = ac // i
            if i + j == b:
                m, n = i, j
                break
    if m is None:
        print("Error: Quadratic does not factor neatly.")
        sys.exit(1)

    gcf1 = math.gcd(a, m)
    gcf2 = math.gcd(n, c)
    if n < 0: gcf2 = -abs(gcf2)
    f1 = a // gcf1
    f2 = m // gcf1

    # --- 2. MANIM TEMPLATE ---
    manim_code = f"""from manim import *
from manim_slides import Slide

class FactoringPresentation(Slide):
    def construct(self):
        title = Text("Factoring Quadratics", color=BLUE).to_edge(UP, buff=0.4)
        self.play(Write(title))
        divider = Line(UP * 2, DOWN * 3, color=GRAY_C, stroke_width=2)
        self.play(Create(divider))
        self.next_slide()
        
        # [Simplified for brevity - insert your full template from before here]
        # Ensure it matches the exact logic you had earlier.
        self.wait()
"""
    
    # --- 3. GENERATION & DIRECTORY MANAGEMENT ---
    problem_name = f"factoring-{a}x2{format_sign(b)}{abs(b)}x{format_sign(c)}{abs(c)}".replace("+", "plus").replace("-", "minus")
    dir_path = f"algebra/{problem_name}"
    
    os.makedirs(dir_path, exist_ok=True)
    with open("temp_manim.py", "w") as f:
        f.write(manim_code)

    subprocess.run(["manim", "temp_manim.py", "FactoringPresentation", "-v", "WARNING", "--disable_caching"], check=True)
    subprocess.run(["manim-slides", "convert", "FactoringPresentation", f"{dir_path}/index.html"], check=True)
    
    # --- 4. DASHBOARD UPDATE ---
    dashboard_path = "index.html"
    display_label = f"{a}x² {format_sign(b)} {abs(b)}x {format_sign(c)} {abs(c)}"
    link_html = f'<li><a href="{dir_path}/index.html">{display_label}</a></li>\n'
    
    if not os.path.exists(dashboard_path):
        with open(dashboard_path, "w") as f:
            f.write("<h1>Math Slides Dashboard</h1><ul></ul>")
            
    with open(dashboard_path, "r") as f:
        content = f.readlines()
        
    index = next((i for i, line in enumerate(content) if "</ul>" in line), len(content))
    if link_html not in content:
        content.insert(index, link_html)
        with open(dashboard_path, "w") as f:
            f.writelines(content)

    os.remove("temp_manim.py")
    
    # --- 5. GIT DEPLOYMENT ---
    print("--> Pushing to GitHub...")
    subprocess.run(["git", "add", "algebra/", "index.html"], check=True)
    subprocess.run(["git", "commit", "-m", f"Add {problem_name}"], check=True)
    subprocess.run(["git", "push"], check=True)
    
    print(f"Success! Slide created at {dir_path}/index.html")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python build_slide.py <a> <b> <c>")
        sys.exit(1)
    build_slides(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))