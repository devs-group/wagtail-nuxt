<template>
  <div>
    <div class="bg-custom-green-bright pt-32 pb-10 min-h-screen relative">
      <div class="flex flex-col items-center mt-6 text-white px-2">
        <div
          class="flex flex-wrap w-full max-w-md font-moret text-xl italic font-bold tracking-widest"
        >
          <p class="flex justify-center items-center w-1/2 h-38">
            {{ aboutUsPage.title }}
          </p>
          <div
            v-for="galleryImage in aboutUsPage.galleryImages"
            :key="galleryImage.id"
            class="w-1/2 h-38 outline-border"
          >
            <img
              :src="galleryImage.image.rendition.url"
              :alt="galleryImage.image.title"
              class="w-full h-full object-cover object-center"
            />
          </div>
          <p
            class="flex flex-col justify-center items-center w-1/2 h-38 outline-border"
          >
            {{ $t('about.follow_us') }}
            <SocialIcon
              :size="20"
              :href="$t('links.instagram')"
              platform="instagram"
            ></SocialIcon>
          </p>
          <p
            class="flex flex-col justify-center items-center w-1/2 h-38 outline-border"
          >
            {{ $t('about.like_us') }}
            <SocialIcon
              :size="20"
              :href="$t('links.facebook')"
              platform="facebook"
            ></SocialIcon>
          </p>
        </div>

        <div
          v-html="aboutUsPage.aboutUsText"
          class="wysiwyg-inject font-monotalic text-sm px-2 mt-20 tracking-wider"
        ></div>

        <div class="font-monotalic text-sm mt-8 tracking-wider">
          <p class="font-moret text-xl italic px-2 font-bold">
            {{ $t('about.legal') }}
          </p>
          <hr class="mt-8 mb-4 opacity-50" />
          <p
            v-html="aboutUsPage.legalText"
            class="wysiwyg-inject mb-4 px-2"
          ></p>
        </div>

        <div class="font-signo self-start text-xs mt-2 px-2 tracking-wider">
          <p v-for="galleryImage in getPhotocredits" :key="galleryImage.id">
            {{ $t('about.photocredit') }} {{ galleryImage.photocredit }}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import gql from 'graphql-tag'
import { pageTitle } from '@/utils'
import SocialIcon from '@/components/SocialIcon/index'

export default {
  components: { SocialIcon },
  computed: {
    getPhotocredits() {
      return this.aboutUsPage.galleryImages.filter(
        (galleryImage) => !!galleryImage.photocredit
      )
    }
  },
  head() {
    return {
      title: pageTitle('About')
    }
  },
  async asyncData({ params, app }) {
    const client = app.apolloProvider.defaultClient
    const response = await client.query({
      query: gql`
        query getAboutUsPage {
          aboutUsPage {
            id
            title
            aboutUsText
            legalText
            galleryImages {
              id
              photocredit
              image {
                id
                rendition(width: 200) {
                  id
                  url
                }
                title
              }
            }
          }
        }
      `
    })
    const data = await response.data
    return {
      ...data
    }
  }
}
</script>

<style lang="scss" scoped>
.outline-border {
  outline: 1px solid white;
}
::v-deep .wysiwyg-inject {
  p {
    margin-bottom: 1rem;
  }
}
</style>
