import sys
import os
import subprocess

def build_chapter_r_lesson():
    # --- 1. MANIM TEMPLATE ---
    manim_code = r"""from manim import *
from manim_slides import Slide
import numpy as np

class SimplifyingExpressions(Slide):
    def construct(self):
        # ---------------------------------------------------------
        # SLIDE 1: Title
        # ---------------------------------------------------------
        title = Text("Chapter R", font_size=40, color=BLUE).to_edge(UP)
        subtitle = Text("Simplifying Expressions & Clearing Parentheses", font_size=36, color=YELLOW).next_to(title, DOWN)
        desc = Text("Evaluating numerical expressions using the order of operations.", font_size=24).next_to(subtitle, DOWN, buff=0.5)
        
        self.play(Write(title), FadeIn(subtitle, shift=DOWN))
        self.play(FadeIn(desc))
        self.next_slide()
        self.play(FadeOut(title), FadeOut(subtitle), FadeOut(desc))

        # ---------------------------------------------------------
        # SLIDE 2: Intro to Radicals
        # ---------------------------------------------------------
        rad_title = Text("Understanding the Radical", font_size=40, color=BLUE).to_edge(UP)
        
        def_box = Rectangle(width=6, height=3, color=WHITE, fill_color=BLACK, fill_opacity=0.8).shift(LEFT * 3)
        def_header = Text("The Square Root", font_size=28, color=YELLOW).move_to(def_box.get_top() + DOWN * 0.4)
        def_text = Tex(
            r"The operation that asks:\\"
            r"\textbf{What number can you square}\\"
            r"\textbf{to get this value?}",
            font_size=24
        ).move_to(def_box.get_center())
        
        ex_box = Rectangle(width=5, height=4, color=ORANGE, fill_color=BLACK, fill_opacity=0.8).shift(RIGHT * 3)
        
        ex1_math = MathTex(r"\sqrt{9} = 3", font_size=36).move_to(ex_box.get_top() + DOWN * 1)
        ex1_text = Tex(r"Because $3 \times 3 = 9$", font_size=24, color=LIGHT_GRAY).next_to(ex1_math, DOWN, buff=0.2)
        
        ex2_math = MathTex(r"\sqrt{81} = 9", font_size=36).next_to(ex1_text, DOWN, buff=0.5)
        ex2_text = Tex(r"Because $9 \times 9 = 81$", font_size=24, color=LIGHT_GRAY).next_to(ex2_math, DOWN, buff=0.2)

        self.play(Write(rad_title))
        self.play(Create(def_box), Write(def_header), FadeIn(def_text))
        self.play(Create(ex_box))
        self.play(Write(ex1_math), FadeIn(ex1_text))
        self.play(Write(ex2_math), FadeIn(ex2_text))
        self.next_slide()
        
        self.play(FadeOut(rad_title), FadeOut(def_box), FadeOut(def_header), FadeOut(def_text), 
                  FadeOut(ex_box), FadeOut(ex1_math), FadeOut(ex1_text), FadeOut(ex2_math), FadeOut(ex2_text))

        # ---------------------------------------------------------
        # SLIDE 3: Radical Practice
        # ---------------------------------------------------------
        prac_title = Text("You Try: Radicals", font_size=40, color=BLUE).to_edge(UP)
        timer_text = Text("1.5 Minutes", font_size=24, color=RED).to_corner(UR)
        
        self.play(Write(prac_title), FadeIn(timer_text))

        grid_group = VGroup()
        q1 = MathTex(r"\sqrt{16} = ?", font_size=40)
        q2 = MathTex(r"\sqrt{25} = ?", font_size=40)
        q3 = MathTex(r"\sqrt{100} = ?", font_size=40)
        q4 = MathTex(r"\sqrt{144} = ?", font_size=40)
        
        questions = VGroup(q1, q2, q3, q4).arrange_in_grid(rows=2, cols=2, buff=(2.5, 1.5)).shift(DOWN * 0.5)
        
        self.play(Write(questions))
        self.next_slide()

        a1 = MathTex(r"\sqrt{16} = 4", font_size=40).move_to(q1)
        r1 = Tex(r"Because $4 \times 4 = 16$", font_size=20, color=YELLOW).next_to(a1, DOWN)
        self.play(Transform(q1, a1), FadeIn(r1))
        self.next_slide()

        a2 = MathTex(r"\sqrt{25} = 5", font_size=40).move_to(q2)
        r2 = Tex(r"Because $5 \times 5 = 25$", font_size=20, color=YELLOW).next_to(a2, DOWN)
        self.play(Transform(q2, a2), FadeIn(r2))
        self.next_slide()

        a3 = MathTex(r"\sqrt{100} = 10", font_size=40).move_to(q3)
        r3 = Tex(r"Because $10 \times 10 = 100$", font_size=20, color=YELLOW).next_to(a3, DOWN)
        self.play(Transform(q3, a3), FadeIn(r3))
        self.next_slide()

        a4 = MathTex(r"\sqrt{144} = 12", font_size=40).move_to(q4)
        r4 = Tex(r"Because $12 \times 12 = 144$", font_size=20, color=YELLOW).next_to(a4, DOWN)
        self.play(Transform(q4, a4), FadeIn(r4))
        self.next_slide()

        self.play(FadeOut(prac_title), FadeOut(timer_text), FadeOut(questions), FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4))

        # ---------------------------------------------------------
        # SLIDE 4: Order of Operations
        # ---------------------------------------------------------
        ooo_title = Text("Order of Operations", font_size=40, color=BLUE).to_edge(UP)
        
        steps = VGroup(
            Tex(r"\textbf{1. Grouping Symbols:} (), [], \{\}, radicals.", font_size=28),
            Tex(r"\textit{Do innermost first.}", font_size=24, color=RED).shift(RIGHT * 0.5),
            Tex(r"\textbf{2. Exponents:} Powers and roots.", font_size=28),
            Tex(r"\textbf{3. Multiply \& Divide:} Left to right.", font_size=28),
            Tex(r"\textbf{4. Add \& Subtract:} Left to right.", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).shift(LEFT * 2)

        self.play(Write(ooo_title))
        self.play(Write(steps[0]))
        self.play(FadeIn(steps[1], shift=RIGHT))
        
        box1 = Square(side_length=3, color=WHITE).shift(RIGHT * 3)
        box2 = Square(side_length=2, color=YELLOW).move_to(box1)
        box3 = Square(side_length=1, color=RED).move_to(box1)
        
        self.play(Create(box1))
        self.play(Create(box2))
        self.play(Create(box3))
        self.next_slide()

        self.play(Write(steps[2]))
        self.next_slide()
        
        self.play(Write(steps[3]))
        self.next_slide()
        
        self.play(Write(steps[4]))
        self.next_slide()

        self.play(FadeOut(ooo_title), FadeOut(steps), FadeOut(box1), FadeOut(box2), FadeOut(box3))

        # ---------------------------------------------------------
        # SLIDE 5: Guided Practice (I Do)
        # ---------------------------------------------------------
        gp_title = Text("Guided Practice: Step-by-Step", font_size=36, color=BLUE).to_edge(UP)
        eq_group = VGroup()
        
        # Split string exactly where we want to highlight: line1[1] is \sqrt{64}
        line1 = MathTex(r"7 - \{8 + 4[2 - (5 - ", r"\sqrt{64}", r")^2]\}", font_size=36)
        eq_group.add(line1)
        eq_group.arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(UP * 1.5)
        
        self.play(Write(gp_title))
        self.play(Write(line1))
        self.next_slide()

        # Indicate innermost radical (much slower)
        ind1 = Indicate(line1[1], color=YELLOW, scale_factor=1.2, run_time=2.0) 
        self.play(ind1)
        
        # Split string for (5 - 8)
        line2 = MathTex(r"= 7 - \{8 + 4[2 - ", r"(5 - 8)", r"^2]\}", font_size=36)
        eq_group.add(line2)
        eq_group.arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(UP * 1.5)
        self.play(Write(line2))
        self.next_slide()

        # Indicate innermost parenthesis
        ind2 = Indicate(line2[1], color=YELLOW, scale_factor=1.2, run_time=2.0)
        self.play(ind2)
        
        # Split string for (-3)^2
        line3 = MathTex(r"= 7 - \{8 + 4[2 - ", r"(-3)^2", r"]\}", font_size=36)
        eq_group.add(line3)
        eq_group.arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(UP * 1.5)
        self.play(Write(line3))
        self.next_slide()

        # Indicate exponent
        ind3 = Indicate(line3[1], color=YELLOW, scale_factor=1.2, run_time=2.0)
        self.play(ind3)
        
        # Split string for [2 - 9]
        line4 = MathTex(r"= 7 - \{8 + 4", r"[2 - 9]", r"\}", font_size=36)
        eq_group.add(line4)
        eq_group.arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(UP * 1.5)
        self.play(Write(line4))
        self.next_slide()

        # Indicate bracket
        ind4 = Indicate(line4[1], color=YELLOW, scale_factor=1.2, run_time=2.0)
        self.play(ind4)
        
        # Split string for 4[-7]
        line5 = MathTex(r"= 7 - \{8 + ", r"4[-7]", r"\}", font_size=36)
        eq_group.add(line5)
        eq_group.arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(UP * 1.5)
        self.play(Write(line5))
        self.next_slide()

        # Indicate multiplication
        ind5 = Indicate(line5[1], color=YELLOW, scale_factor=1.2, run_time=2.0)
        self.play(ind5)
        
        # Split string for \{8 - 28\}
        line6 = MathTex(r"= 7 - ", r"\{8 - 28\}", font_size=36)
        eq_group.add(line6)
        eq_group.arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(UP * 1.5)
        self.play(Write(line6))
        self.next_slide()

        # Indicate brace
        ind6 = Indicate(line6[1], color=YELLOW, scale_factor=1.2, run_time=2.0) 
        self.play(ind6)
        
        # Split string for 7 - \{-20\}
        line7 = MathTex(r"= ", r"7 - \{-20\}", font_size=36)
        eq_group.add(line7)
        eq_group.arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(UP * 1.5)
        self.play(Write(line7))
        self.next_slide()

        ind7 = Indicate(line7[1], color=YELLOW, scale_factor=1.2, run_time=2.0)
        self.play(ind7)

        # Final Answer
        line8 = MathTex(r"= 27", font_size=48, color=GREEN)
        eq_group.add(line8)
        eq_group.arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(UP * 1.5)
        self.play(Write(line8))
        self.next_slide()

        self.play(FadeOut(gp_title), FadeOut(eq_group))

        # ---------------------------------------------------------
        # SLIDE 6: Independent Practice (You Do)
        # ---------------------------------------------------------
        yd_title = Text("You Do: Step-by-Step", font_size=36, color=ORANGE).to_edge(UP)
        yd_timer = Text("1.5 Minutes", font_size=24, color=RED).to_corner(UR)
        yd_eq_group = VGroup()
        
        # yline1[1] is \sqrt{121}, yline1[3] is (-1 - 3)
        yline1 = MathTex(r"50 - \{2 - [", r"\sqrt{121}", r" + 3", r"(-1 - 3)", r"^2]\}", font_size=36)
        yd_eq_group.add(yline1)
        yd_eq_group.arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(UP * 1.5)
        
        self.play(Write(yd_title), FadeIn(yd_timer))
        self.play(Write(yline1))
        self.next_slide()

        # Indicate innermost elements
        y_ind1a = Indicate(yline1[1], color=YELLOW, scale_factor=1.2, run_time=2.0)
        y_ind1b = Indicate(yline1[3], color=YELLOW, scale_factor=1.2, run_time=2.0) 
        self.play(y_ind1a, y_ind1b)
        
        yline2 = MathTex(r"= 50 - \{2 - [11 + 3", r"(-4)^2", r"]\}", font_size=36)
        yd_eq_group.add(yline2)
        yd_eq_group.arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(UP * 1.5)
        self.play(Write(yline2))
        self.next_slide()

        y_ind2 = Indicate(yline2[1], color=YELLOW, scale_factor=1.2, run_time=2.0)
        self.play(y_ind2)
        
        yline3 = MathTex(r"= 50 - \{2 - [11 + ", r"3(16)", r"]\}", font_size=36)
        yd_eq_group.add(yline3)
        yd_eq_group.arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(UP * 1.5)
        self.play(Write(yline3))
        self.next_slide()

        y_ind3 = Indicate(yline3[1], color=YELLOW, scale_factor=1.2, run_time=2.0)
        self.play(y_ind3)
        
        yline4 = MathTex(r"= 50 - \{2 - ", r"[11 + 48]", r"\}", font_size=36)
        yd_eq_group.add(yline4)
        yd_eq_group.arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(UP * 1.5)
        self.play(Write(yline4))
        self.next_slide()

        y_ind4 = Indicate(yline4[1], color=YELLOW, scale_factor=1.2, run_time=2.0)
        self.play(y_ind4)
        
        yline5 = MathTex(r"= 50 - ", r"\{2 - 59\}", font_size=36)
        yd_eq_group.add(yline5)
        yd_eq_group.arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(UP * 1.5)
        self.play(Write(yline5))
        self.next_slide()

        y_ind5 = Indicate(yline5[1], color=YELLOW, scale_factor=1.2, run_time=2.0)
        self.play(y_ind5)
        
        yline6 = MathTex(r"= ", r"50 - \{-57\}", font_size=36)
        yd_eq_group.add(yline6)
        yd_eq_group.arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(UP * 1.5)
        self.play(Write(yline6))
        self.next_slide()

        y_ind6 = Indicate(yline6[1], color=YELLOW, scale_factor=1.2, run_time=2.0)
        self.play(y_ind6)
        
        yline7 = MathTex(r"= 107", font_size=48, color=GREEN)
        yd_eq_group.add(yline7)
        yd_eq_group.arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(UP * 1.5)
        self.play(Write(yline7))
        self.next_slide()

        self.play(FadeOut(yd_title), FadeOut(yd_timer), FadeOut(yd_eq_group))

        # ---------------------------------------------------------
        # SLIDE 7: Textbook Practice
        # ---------------------------------------------------------
        tb_title = Text("Independent Practice", font_size=40, color=BLUE).to_edge(UP)
        tb_sub = Text("Textbook Page R20", font_size=28, color=YELLOW).next_to(tb_title, DOWN)
        tb_timer = Text("4.0 Minutes", font_size=24, color=RED).to_corner(UR)
        
        prob71 = MathTex(r"\textbf{71)} \quad 6 - \{-12 + 3[(1 - 6)^2 - 18]\}", font_size=36)
        prob72 = MathTex(r"\textbf{72)} \quad -5 - \{4 - 6[(2 - 8)^2 - 31]\}", font_size=36)
        
        tb_probs = VGroup(prob71, prob72).arrange(DOWN, buff=1.0)
        
        self.play(Write(tb_title), FadeIn(tb_sub), FadeIn(tb_timer))
        self.play(Write(tb_probs))
        self.next_slide()

        self.play(FadeOut(tb_title), FadeOut(tb_sub), FadeOut(tb_timer), FadeOut(tb_probs))

        # ---------------------------------------------------------
        # SLIDE 8: Group Work
        # ---------------------------------------------------------
        gw_title = Text("Group Work", font_size=48, color=GREEN).to_edge(UP)
        gw_sub = Text("Page R20", font_size=32, color=YELLOW).next_to(gw_title, DOWN)
        
        gw_list = VGroup(
            Text("65 (a-f)", font_size=28),
            Text("66 (a-f)", font_size=28),
            Text("67 (d, f)", font_size=28),
            Text("68 (d, e, f)", font_size=28),
            Text("69, 70, 73", font_size=28),
            Text("74, 75, 76", font_size=28)
        ).arrange_in_grid(rows=3, cols=2, buff=(1.5, 0.8))
        
        self.play(Write(gw_title), FadeIn(gw_sub))
        self.play(FadeIn(gw_list, shift=UP))
        self.next_slide()
"""
    
    # --- 2. GENERATION & DIRECTORY MANAGEMENT ---
    dir_path = "precalc/chapter_r_expressions" 
    
    os.makedirs(dir_path, exist_ok=True)
    with open("temp_manim_chap_r.py", "w") as f:
        f.write(manim_code)

    subprocess.run(["manim", "temp_manim_chap_r.py", "SimplifyingExpressions", "-v", "WARNING", "--disable_caching"], check=True)
    subprocess.run(["manim-slides", "convert", "SimplifyingExpressions", f"{dir_path}/index.html"], check=True)
    
    # --- 3. DASHBOARD UPDATE ---
    dashboard_path = "index.html"
    display_label = "Precalculus: Chapter R - Simplifying Expressions"
    link_html = f'<li><a href="{dir_path}/index.html">{display_label}</a></li>\n'
    
    if not os.path.exists(dashboard_path):
        with open(dashboard_path, "w") as f:
            f.write("<h1>Math Slides Dashboard</h1>\n<ul>\n</ul>")
            
    with open(dashboard_path, "r") as f:
        content = f.readlines()
        
    index = next((i for i, line in enumerate(content) if "</ul>" in line), len(content))
    if link_html not in content:
        content.insert(index, link_html)
        with open(dashboard_path, "w") as f:
            f.writelines(content)

    os.remove("temp_manim_chap_r.py")
    
    # --- 4. GIT DEPLOYMENT ---
    print("--> Pushing to GitHub...")
    subprocess.run(["git", "add", "precalc/", "index.html"], check=True)
    subprocess.run(["git", "commit", "-m", "Add Precalc Chapter R Simplifying Expressions Lesson"], check=True)
    subprocess.run(["git", "push"], check=True)
    
    print(f"Success! Slide created at {dir_path}/index.html")

if __name__ == "__main__":
    build_chapter_r_lesson()