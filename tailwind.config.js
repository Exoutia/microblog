/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/templates/**/*.html",
    "./node_modules/flowbite/**/*.js",   
    "./app/static/**/*.js",
  ],
  dark: "class",
  theme: {
    extend: {},
  },
  plugins: [
    require("flowbite/plugin"),
  ],
}

