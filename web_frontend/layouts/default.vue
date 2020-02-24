<template>
  <div>
    <top-bar @open="menuIsOpen = $event" class="absolute" />
    <nuxt />
  </div>
</template>
<script>
import TopBar from '@/components/TopBar'
import { pageTitle } from '@/utils'

export default {
  head() {
    return {
      title: pageTitle(),
      bodyAttrs: {
        class: 'overflow-x-hidden relative'
      },
      htmlAttrs: {
        class: `overflow-x-hidden ${this.menuIsOpen ? 'overflow-y-hidden' : ''}`
      }
    }
  },
  components: {
    TopBar
  },
  data() {
    return {
      menuIsOpen: false
    }
  }
}
</script>

<style lang="scss">
.slide-in-from-right-enter-active,
.slide-in-from-right-leave-active {
  transition: transform 0.5s;
}
.slide-in-from-right-enter,
.slide-in-from-right-leave-to {
  transform: translate3d(100%, 0, 0);
}

.slide-in-from-left-enter-active,
.slide-in-from-left-leave-active {
  transition: transform 0.5s;
}
.slide-in-from-left-enter,
.slide-in-from-left-leave-to {
  transform: translate3d(-100%, 0, 0);
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}
.flip-horizontal-enter-active {
  transition: transform 0.25s ease-out;
}
.flip-horizontal-leave-active {
  transition: transform 0.25s ease-in;
}
.flip-horizontal-enter,
.flip-horizontal-leave-to {
  transform: rotate3d(0, 1, 0, 90deg);
}
.fade-scale-enter-active,
.fade-scale-leave-active {
  position: absolute !important;
  transition: opacity 0.4s, transform 0.8s;
}
.fade-scale-enter,
.fade-scale-leave-to {
  transform: scale3d(3, 3, 3);
  opacity: 0;
}
</style>
