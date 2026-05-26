import sys
import os
import math
import subprocess

def format_sign(num):
    return "+" if num >= 0 else "-"

def build_slides(a, b, c):
    # --- 1. ALGEBRAIC LOGIC (AC METHOD) ---
    ac = a * c
    m, n = None, None
    
    # Find factors of a*c that sum to b
    for i in range(-abs(ac) - 1, abs(ac) + 2):
        if i == 0: continue
        if ac % i == 0:
            j = ac // i
            if i + j == b:
                m, n = i, j
                break
                
    if m is None:
        print("Error: Quadratic does not factor neatly over integers.")
        sys.exit(1)

    # Calculate GCFs for grouping: (ax^2 + mx) + (nx + c)
    gcf1 = math.gcd(a, m)
    gcf2 = math.gcd(n, c)
    if n < 0: gcf2 = -abs(gcf2) # Pull out negative if 3rd term is negative

    # Calculate the inner binomial (f1*x + f2)
    f1 = a // gcf1
    f2 = m // gcf1

    # --- 2. MANIM TEMPLATE ---
    # We maintain your exact array indices for MathTex by splitting the dynamic strings exactly like your original script.
    manim_code = f"""from manim import *
from manim_slides import Slide

class FactoringPresentation(Slide):
    def construct(self):
        # --- COLOR DEFINITIONS ---
        X_COLOR = "#228B22"       
        MAGIC_COLOR = "#FF8C00"   

        # --- TITLE SYSTEM ---
        title = Text("Factoring Quadratics", color=BLUE).to_edge(UP, buff=0.4)
        self.play(Write(title))
        
        divider = Line(UP * 2, DOWN * 3, color=GRAY_C, stroke_width=2)
        self.play(Create(divider))
        self.wait()
        self.next_slide()

        text_position = LEFT * 3.5 + UP * 0.5

        # --- STEP 1 ---
        inst_1 = MarkupText(
            "<b>The Challenge:</b>\\nFactor the given quadratic\\nexpression completely.",
            font_size=22
        ).move_to(text_position)
        
        eq_1 = MathTex("{a}", "x", "^2", "{format_sign(b)}", "{abs(b)}", "x", "{format_sign(c)} {abs(c)}").move_to(RIGHT * 3 + UP * 1.5)
        eq_1[1].set_color(X_COLOR)     
        eq_1[2].set_color(WHITE)       
        eq_1[4].set_color(MAGIC_COLOR) 
        eq_1[5].set_color(X_COLOR)     
        
        self.play(FadeIn(inst_1), Write(eq_1))
        self.next_slide()

        # --- STEP 2 ---
        inst_2 = MarkupText(
            "<b>Step 1: AC Method</b>\\nFind two numbers that\\nmultiply to <i>a × c</i> ({ac})\\nand add to <i>b</i> ({b}).\\n\\nMagic numbers: <span color='#FF8C00'>{m}</span> and <span color='#FF8C00'>{n}</span>.",
            font_size=20
        ).move_to(text_position)
        
        self.play(FadeOut(inst_1), FadeIn(inst_2))
        self.next_slide()

        # --- STEP 3 ---
        inst_3 = MarkupText(
            "<b>Step 2: Rewrite</b>\\nSplit the middle term ({b}x)\\nusing our magic numbers\\n{m} and {n}.",
            font_size=20
        ).move_to(text_position)
        
        eq_2 = MathTex("= {a}", "x", "^2", "{format_sign(m)}", "{abs(m)}", "x", "{format_sign(n)}", "{abs(n)}", "x", "{format_sign(c)} {abs(c)}")
        eq_2.next_to(eq_1, DOWN, buff=0.4, aligned_edge=LEFT)

        eq_2[1].set_color(X_COLOR)     
        eq_2[4].set_color(MAGIC_COLOR) 
        eq_2[5].set_color(X_COLOR)     
        eq_2[7].set_color(MAGIC_COLOR) 
        eq_2[8].set_color(X_COLOR)     
        
        self.play(FadeOut(inst_2), FadeIn(inst_3))
        self.play(Write(eq_2))
        self.next_slide()

        # --- STEP 4 ---
        inst_4 = MarkupText(
            "<b>Step 3: Grouping</b>\\nGroup the first two terms\\nand the last two terms.",
            font_size=20
        ).move_to(text_position)
        
        eq_3 = MathTex("= ({a}", "x", "^2", "{format_sign(m)}", "{abs(m)}", "x", ") {format_sign(n)} (", "{abs(n)}", "x", "{format_sign(c)} {abs(c)})")
        eq_3.next_to(eq_1, DOWN, buff=0.4, aligned_edge=LEFT)

        eq_3[1].set_color(X_COLOR)     
        eq_3[4].set_color(MAGIC_COLOR) 
        eq_3[5].set_color(X_COLOR)     
        eq_3[7].set_color(MAGIC_COLOR) 
        eq_3[8].set_color(X_COLOR)     
        
        self.play(FadeOut(inst_3), FadeIn(inst_4))
        self.play(FadeOut(eq_2), FadeIn(eq_3)) 
        self.next_slide()

        # --- STEP 5 ---
        inst_5 = MarkupText(
            "<b>Step 4: Factor GCF</b>\\nExtract the Greatest Common\\nFactor from each binomial group.",
            font_size=20
        ).move_to(text_position)
        
        eq_4 = MathTex("= {gcf1}", "x", "({f1}", "x", "{format_sign(f2)} {abs(f2)}) {format_sign(gcf2)} {abs(gcf2)}({f1}", "x", "{format_sign(f2)} {abs(f2)})")
        eq_4.next_to(eq_3, DOWN, buff=0.4, aligned_edge=LEFT)
        eq_4[1].set_color(X_COLOR)
        eq_4[3].set_color(X_COLOR)
        eq_4[5].set_color(X_COLOR)
        
        self.play(FadeOut(inst_4), FadeIn(inst_5))
        self.play(Write(eq_4))
        self.next_slide()

        # --- STEP 6 ---
        inst_6 = MarkupText(
            "<b>Step 5: Final Product</b>\\nFactor out the common\\nbinomial block.",
            font_size=20
        ).move_to(text_position)
        
        eq_5 = MathTex("= ({f1}", "x", "{format_sign(f2)} {abs(f2)})({gcf1}", "x", "{format_sign(gcf2)} {abs(gcf2)})", color=GOLD)
        eq_5.next_to(eq_4, DOWN, buff=0.4, aligned_edge=LEFT)
        eq_5[1].set_color(X_COLOR)
        eq_5[3].set_color(X_COLOR)
        
        self.play(FadeOut(inst_5), FadeIn(inst_6))
        self.play(Write(eq_5))
        self.wait()
"""
    
    # --- 3. GENERATION & DIRECTORY MANAGEMENT ---
    problem_name = f"factoring-{a}x2{format_sign(b)}{abs(b)}x{format_sign(c)}{abs(c)}".replace("+", "plus").replace("-", "minus")
    dir_path = f"algebra/{problem_name}"
    os.makedirs(dir_path, exist_ok=True)
    
    with open("temp_manim.py", "w") as f:
        f.write(manim_code)

    print(f"--> Rendering Manim frames for {a}x^2 + {b}x + {c}...")
    subprocess.run(["manim", "temp_manim.py", "FactoringPresentation", "-v", "WARNING", "--disable_caching"], check=True)
    
    print("--> Converting to HTML slides...")
    subprocess.run(["manim-slides", "convert", "FactoringPresentation", f"{dir_path}/index.html"], check=True)
    
   # --- 4. DASHBOARD UPDATE ---
    dashboard_path = "math-slides/index.html"
    # Format the link label cleanly
    display_label = f"{a}x² {format_sign(b)} {abs(b)}x {format_sign(c)} {abs(c)}"
    # --- Update your dashboard link logic ---
    # Now the link is relative to the root index.html
    link_html = f'<li><a href="algebra/{problem_name}/index.html">{display_label}</a></li>\n'
    
    # Ensure the dashboard file exists
    if not os.path.exists(dashboard_path):
        with open(dashboard_path, "w") as f:
            f.write("<h1>Math Slides Dashboard</h1>\n<h2>Algebra</h2>\n<ul>\n</ul>")
            
    with open(dashboard_path, "r") as f:
        content = f.readlines()
        
    # Find the index of the line containing </ul>
    try:
        # Search for the list closing tag
        index = next(i for i, line in enumerate(content) if "</ul>" in line)
        
        # Only add if the link isn't already there
        if link_html not in content:
            content.insert(index, link_html)
            with open(dashboard_path, "w") as f:
                f.writelines(content)
                
    except StopIteration:
        # If </ul> is missing, just append a new list to the end
        with open(dashboard_path, "a") as f:
            f.write(f"\n<ul>\n{link_html}</ul>\n")

    # Cleanup temp files
    os.remove("temp_manim.py")
    
    # --- 5. GIT DEPLOYMENT ---
    print("--> Pushing to GitHub...")
    subprocess.run(["git", "add", "math-slides/"], check=True)
    subprocess.run(["git", "commit", "-m", f"Add factoring slide for {a}x^2 + {b}x + {c}"], check=True)
    subprocess.run(["git", "push"], check=True)
    
    print(f"Success! Slide deck created at {dir_path}/index.html and pushed to repo.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python build_slide.py <a> <b> <c>")
        print("Example: python build_slide.py 6 7 2")
        sys.exit(1)
        
    a_val, b_val, c_val = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    build_slides(a_val, b_val, c_val)