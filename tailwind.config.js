const colors = require("tailwindcss/colors");

module.exports = {
  content: [],
  theme: {
    boxShadow: {
      lg: "0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(51, 65, 85, 0.5)",
    },
    extend: {
      fontFamily: {
        sans: ["Mulish", "sans-serif"],
      },
      colors: {
        primary: "#f5c226",
        secondary: "#009fcd",
        back: "#1D1F23",
        slate500: "#64748b",
        slate700: "#334155",
      },
    },
  },
  plugins: [require("@tailwindcss/line-clamp")],
};
