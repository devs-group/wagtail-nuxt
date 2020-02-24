<template>
  <div>
    <div
      class="bg-custom-gold z-20 font-signo text-sm text-white tracking-wide pt-14 px-2 pb-10 min-h-screen relative"
    >
      <div class="flex flex-row justify-between items-center">
        <h1 class="font-moret italic font-bold text-2xl tracking-widest">
          {{ $t('contact.contact_us') }}
        </h1>
        <CloseButton @click="$router.push(localePath('/'))"></CloseButton>
      </div>
      <div class="mt-12 relative">
        <input
          :placeholder="$t('contact.your_name')"
          class="bg-transparent font-hairline tracking-widest focus:outline-none placeholder-white border-b
          border-gray-400 block w-full appearance-none leading-normal"
          type="text"
        />
        <input
          :placeholder="$t('contact.your_email')"
          class="bg-transparent font-hairline tracking-widest mt-4 focus:outline-none placeholder-white border-b
          border-gray-400 block w-full appearance-none leading-normal"
          type="email"
        />
        <div class="mt-4">
          <span class="text-base">{{ $t('contact.message') }}</span>
          <textarea
            class="bg-transparent font-hairline tracking-widestfocus:outline-none placeholder-white border
          border-gray-400 block outline-none p-2 w-full appearance-none leading-normal"
            rows="12"
          />
        </div>
        <button
          class="bg-transparent font-light tracking-widest mt-4 focus:outline-none border-b border-gray-400"
        >
          {{ $t('contact.send') }}
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { pageTitle } from '@/utils'
import CloseButton from '@/components/shared/CloseButton'

export default {
  components: { CloseButton },
  head() {
    return {
      title: pageTitle('Inspiration')
    }
  }
}
</script>
