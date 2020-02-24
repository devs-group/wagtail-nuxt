<template>
  <div
    v-body-scroll-lock="menuIsOpen"
    class="text-white flex justify-between flex-row w-full p-2 pt-4 z-20"
  >
    <transition name="slide-in-from-left">
      <Menu @menuItemClick="toggleMenu" v-if="menuIsOpen" />
    </transition>
    <div>
      <nuxt-link :to="localePath('/')">
        <img
          class="mt-6 ml-4"
          width="68"
          height="50"
          src="@/assets/youme_white.png"
        />
      </nuxt-link>
    </div>
    <div class="flex align-center items-end">
      <div class="mr-4 font-moret text-2xl leading-none">
        <div>
          <a v-if="$i18n.locale === 'en'" :href="switchLocalePath('de')">DE</a>
          <a v-else-if="$i18n.locale === 'de'" :href="switchLocalePath('en')"
            >EN</a
          >
        </div>
      </div>
      <burger-button :open="menuIsOpen" @click="toggleMenu" />
    </div>
  </div>
</template>
<script>
import BurgerButton from './BurgerButton'
import Menu from './Menu'

export default {
  components: {
    BurgerButton,
    Menu
  },
  data() {
    return {
      menuIsOpen: false,
      currentLanguage: ''
    }
  },
  mounted() {
    const lang = this.$router.history.current.query.lang
    if (lang) {
      this.currentLanguage = lang.toUpperCase()
    } else {
      this.currentLanguage = 'EN'
    }
  },
  methods: {
    toggleMenu() {
      this.menuIsOpen = !this.menuIsOpen
      this.$emit('open', this.menuIsOpen)
    },
    changeLanguage() {
      this.$nuxt.$router.replace({ path: '?lang=de' })
    }
  }
}
</script>
