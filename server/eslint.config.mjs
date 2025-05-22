import js from "@eslint/js";
import globals from "globals";
import pluginReact from "eslint-plugin-react";
import { defineConfig } from "eslint/config";

export default defineConfig([
  {
    files: ["**/*.{js,mjs,cjs,jsx}"],

    // Set language options to support modern JS and global environments
    languageOptions: {
      ecmaVersion: 2022,
      sourceType: "module",
      globals: {
        ...globals.browser,
        ...globals.node,
      },
      settings: {
        react: {
          version: "detect",
        },
      },
    },

    // Use ESLint's core recommended rules and React's recommended rules
    plugins: {
      react: pluginReact,
    },

    rules: {
      ...js.configs.recommended.rules,
      ...pluginReact.configs.recommended.rules,

      // 🔧 Fixable rules to match your JSHint output:

      // ✅ Missing semicolon
      semi: ["error", "always"],

      // ✅ Prefer dot notation over bracket notation where possible
      "dot-notation": ["warn"],

      // ✅ Use double quotes consistently
      quotes: ["error", "double", { avoidEscape: true }],

      // ✅ Detect and warn about unused variables
      "no-unused-vars": ["warn"],

      // ✅ Disallow unnecessary brackets around properties
      "no-useless-computed-key": "warn",

      // ✅ Disallow object property keys that can be literals
      "quote-props": ["error", "as-needed"],

      // ✅ Require consistent spacing inside braces
      "object-curly-spacing": ["error", "always"],

      // ✅ Enforce consistent indentation (2 spaces)
      indent: ["error", 2],

      // ✅ Enforce newline at end of file
      "eol-last": ["error", "always"],
    },
  },
]);
