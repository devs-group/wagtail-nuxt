<template>
  <div v-if="href">
    <a :href="href" target="_blank">
      <img
        :src="require(`@/assets/icons/${platform}_icon_white.svg`)"
        :width="size"
        :height="size"
      />
    </a>
  </div>
</template>

<script>
export default {
  name: 'SocialIcon',
  props: {
    href: {
      type: String,
      required: true
    },
    size: {
      type: Number,
      default: 32
    },
    platform: {
      type: String,
      default: 'instagram',
      validator: (platform) => {
        platform = platform.toLowerCase()
        switch (platform) {
          case 'instagram':
            return true
          case 'facebook':
            return true
          case 'twitter':
            return true
          case 'homepage':
            return true
          default:
            return false
        }
      }
    }
  }
}
</script>
