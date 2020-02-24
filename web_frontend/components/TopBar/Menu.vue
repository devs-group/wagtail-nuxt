<template>
  <div
    class="bg-black w-screen h-screen fixed z-10 flex justify-center items-center top-0 left-0"
  >
    <div class="text-center text-4xl tracking-7-5 italic font-bold font-moret">
      <p @click="navigate(localePath('/'))" class="mb-1 cursor-pointer">
        {{ $t('menu.home') }}
      </p>
      <a
        @click="navigate(localePath('/'), '#locals')"
        class="mb-1 cursor-pointer"
      >
        {{ $t('menu.locals') }}
      </a>
      <p
        @click="navigate(localePath('/interests'))"
        class="mb-1 cursor-pointer"
      >
        {{ $t('menu.interests') }}
      </p>
      <p @click="navigate(localePath('/about'))" class="mb-1 cursor-pointer">
        {{ $t('menu.about') }}
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Name',
  methods: {
    navigate(route, hash) {
      this.$router.push(
        route,
        () => {
          this.scrollToHash(hash)
        },
        () => {
          this.scrollToHash(hash)
        }
      )
      this.$emit('menuItemClick')
    },
    scrollToHash(hash) {
      if (hash) {
        setTimeout(() => {
          this.$scrollTo(hash)
        }, 100)
      }
    }
  }
}
</script>
