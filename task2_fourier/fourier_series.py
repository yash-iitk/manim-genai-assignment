from manim import *
import numpy as np

class FourierSquareWave(Scene):
    def construct(self):

        # Title
        title = Text(
            "Fourier Series: Square Wave",
            font_size=36,
            color=WHITE
        ).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Axes
        axes = Axes(
            x_range=[0, 4 * np.pi, np.pi],
            y_range=[-2, 2, 1],
            x_length=10,
            y_length=5,
            axis_config={"color": WHITE},
        ).shift(DOWN * 0.3)
        self.play(Create(axes))
        self.wait(0.5)

        # Colors for 5 harmonics
        colors = [BLUE, GREEN, RED, YELLOW, PURPLE]
        n_values = [1, 3, 5, 7, 9]

        # Running sum
        running_terms = []

        for i, n in enumerate(n_values):

            # Individual harmonic
            def make_harmonic(n):
                return lambda x: (4 / (np.pi * n)) * np.sin(n * x)

            harmonic_func = make_harmonic(n)

            harmonic_curve = axes.plot(
                harmonic_func,
                color=colors[i],
                stroke_width=2,
                use_smoothing=True
            )

            label = Text(
                f"n = {n}",
                font_size=24,
                color=colors[i]
            ).to_corner(UR).shift(DOWN * (0.5 * i + 1))

            self.play(
                Create(harmonic_curve),
                FadeIn(label),
                run_time=1.5
            )
            self.wait(0.5)

            # Add to running sum
            running_terms.append(harmonic_func)

            # Cumulative sum curve
            def make_sum(terms):
                def f(x):
                    return sum(t(x) for t in terms)
                return f

            sum_func = make_sum(list(running_terms))

            sum_curve = axes.plot(
                sum_func,
                color=ORANGE,
                stroke_width=3,
                use_smoothing=True
            )

            sum_label = Text(
                f"Sum (1 to n={n})",
                font_size=22,
                color=ORANGE
            ).to_edge(DOWN)

            self.play(
                Create(sum_curve),
                FadeIn(sum_label),
                run_time=1.5
            )
            self.wait(1)

            # Remove sum before next iteration
            # (keep harmonics visible)
            if i < len(n_values) - 1:
                self.play(
                    FadeOut(sum_curve),
                    FadeOut(sum_label),
                    FadeOut(harmonic_curve),
                    run_time=0.5
                )
            else:
                # Last iteration - keep final sum
                self.wait(2)

        self.wait(2)