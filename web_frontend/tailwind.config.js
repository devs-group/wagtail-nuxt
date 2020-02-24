/*
 ** TailwindCSS Configuration File
 **
 ** Docs: https://tailwindcss.com/docs/configuration
 ** Default: https://github.com/tailwindcss/tailwindcss/blob/master/stubs/defaultConfig.stub.js
 */
module.exports = {
  theme: {
    fontFamily: {
      monotalic: 'monotalic, sans-serif',
      moret: 'moret, serif',
      signo: 'signo sans-serif'
    },
    extend: {
      colors: {
        'custom-brown': '#886562',
        'custom-gold': '#877646',
        'custom-green': '#234F40',
        'custom-green-bright': '#828536',
        'custom-green-brightest': '#818564',
        'custom-turquoise': '#20696b'
      },
      letterSpacing: {
        '7-5': '7.5px'
      },
      fontSize: {
        xxxs: '0.625rem',
        xxs: '0.6875rem',
        '1xl': '1.375rem',
        '5xl': '3.5rem'
      },
      opacity: {
        '35': '.35'
      },
      height: {
        '38': '9.5rem'
      },
      spacing: {
        14: '3.5rem'
      },
      maxWidth: {
        half: '50%'
      }
    }
  },
  variants: {},
  plugins: []
}
