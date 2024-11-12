/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./dengue/templates/**/*.html",
    "./dengue/static/src/**/*.js",
    "./node_modules/flowbite/**/*.js",
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ["General Sans", "sans-serif"],
      },
    },
  },
  plugins: [
    require("flowbite/plugin"),
  ],
}

