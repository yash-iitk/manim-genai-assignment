from manim import *
import numpy as np

class PythagoreanTheoremProof(Scene):
    def construct(self):
        # Define triangle vertices for a 3-4-5 right triangle
        # The right angle will be at A
        A = ORIGIN
        B = 3 * RIGHT
        C = 4 * UP

        # Shift the entire figure to center it better on the screen
        triangle_offset = LEFT * 1.5 + DOWN * 1.5
        A_shifted = A + triangle_offset
        B_shifted = B + triangle_offset
        C_shifted = C + triangle_offset

        # Create the main right triangle
        triangle = Polygon(A_shifted, B_shifted, C_shifted, color=WHITE, stroke_width=4)
        self.play(Create(triangle))
        self.wait(0.5)

        # --- Square and Label for side 'a' (A-B) ---
        side_a_start = A_shifted
        side_a_end = B_shifted
        len_a = np.linalg.norm(side_a_end - side_a_start)
        vec_a = side_a_end - side_a_start
        unit_vec_a = vec_a / len_a
        
        # Perpendicular vector pointing outwards from the triangle (downwards for A-B)
        perp_a_vec = rotate_vector(unit_vec_a, -PI/2) 
        square_a = Polygon(
            side_a_start,
            side_a_end,
            side_a_end + perp_a_vec * len_a,
            side_a_start + perp_a_vec * len_a,
            color=BLUE, fill_opacity=0.7
        )
        label_a = Text("a", font_size=30, color=BLUE).next_to(Line(side_a_start, side_a_end), perp_a_vec * 0.7)
        
        self.play(Create(square_a), Write(label_a))
        self.wait(0.5)

        # --- Square and Label for side 'b' (A-C) ---
        side_b_start = A_shifted
        side_b_end = C_shifted
        len_b = np.linalg.norm(side_b_end - side_b_start)
        vec_b = side_b_end - side_b_start
        unit_vec_b = vec_b / len_b
        
        # Perpendicular vector pointing outwards from the triangle (leftwards for A-C)
        perp_b_vec = rotate_vector(unit_vec_b, PI/2) 
        square_b = Polygon(
            side_b_start,
            side_b_end,
            side_b_end + perp_b_vec * len_b,
            side_b_start + perp_b_vec * len_b,
            color=GREEN, fill_opacity=0.7
        )
        label_b = Text("b", font_size=30, color=GREEN).next_to(Line(side_b_start, side_b_end), perp_b_vec * 0.7)

        self.play(Create(square_b), Write(label_b))
        self.wait(0.5)

        # --- Square and Label for side 'c' (B-C, the hypotenuse) ---
        side_c_start = B_shifted
        side_c_end = C_shifted
        len_c = np.linalg.norm(side_c_end - side_c_start)
        vec_c = side_c_end - side_c_start
        unit_vec_c = vec_c / len_c
        
        # Perpendicular vector pointing outwards from the triangle
        perp_c_vec = rotate_vector(unit_vec_c, PI/2) 
        square_c = Polygon(
            side_c_start,
            side_c_end,
            side_c_end + perp_c_vec * len_c,
            side_c_start + perp_c_vec * len_c,
            color=RED, fill_opacity=0.7
        )
        label_c = Text("c", font_size=30, color=RED).next_to(Line(side_c_start, side_c_end), perp_c_vec * 0.7)

        self.play(Create(square_c), Write(label_c))
        self.wait(1)

        # Display the algebraic identity
        theorem_text = Text("a^2 + b^2 = c^2", font_size=48, color=WHITE).to_edge(UP).shift(DOWN * 0.5)
        self.play(Write(theorem_text))
        self.wait(3)