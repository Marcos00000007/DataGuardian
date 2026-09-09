/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        ink: {
          DEFAULT: "#12182B",
          light: "#1C2440",
        },
        parchment: "#E8E2D0",
        stamp: {
          DEFAULT: "#B23A2E",
          light: "#D1584A",
        },
        signal: "#3E6B6B",
        sage: "#6B7A5E",
      },
      fontFamily: {
        display: ['"Source Serif 4"', "Georgia", "serif"],
        body: ['"Inter"', "system-ui", "sans-serif"],
      },
    },
  },
  plugins: [],
};
