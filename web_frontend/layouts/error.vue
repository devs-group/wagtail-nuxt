<template>
  <div>
    <top-bar @open="menuIsOpen = $event" class="absolute" />
    <div class="bg-custom-brown pt-32 pb-10 min-h-screen relative">
      <div class="text-center mt-6 text-white px-2 text-lg">
        <h1 v-if="error.statusCode === 404">
          {{ $t('error.404') }}
        </h1>
        <h1 v-else>{{ $t('error.error') }}</h1>
      </div>
    </div>
  </div>
</template>
<script>
import TopBar from '@/components/TopBar'
import { pageTitle } from '@/utils'

export default {
  name: 'Error',
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
  props: ['error'],
  data() {
    return {
      menuIsOpen: false
    }
  }
}
</script>
