<template>
  <div class="bg-black border-4 border-gray-400 w-auto justify-around">
    <h1 class="text-white text-center text-xl">{{ title }}</h1>
    <div class="container flex flex-row">
      <div class="w-200 p-5">
        <a :href="href">
          <img :src="src" :alt="alt" />
        </a>
      </div>
      <div class="w-48 text-xs p-5 text-gray-400">
        <span v-html="info"></span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'WagtailImage',
  props: {
    title: {
      type: String,
      required: true
    },
    src: {
      type: String,
      required: true
    },
    alt: {
      type: String,
      default: ''
    },
    href: {
      type: String,
      default: '#'
    },
    info: {
      type: String,
      required: true
    }
  }
}
</script>
