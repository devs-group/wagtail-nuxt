export default {
  methods: {
    getFirstLocationGalleryImage(location) {
      if (location.LocationGalleryImageFk.length === 0) {
        return ''
      }
      if (!location.LocationGalleryImageFk[0].imageFk) {
        return ''
      }
      return location.LocationGalleryImage[0].imageFk.rendition.url
    },
    getPerProfileLocationGalleryImage(location) {
      if (location.locationImageRelation.length === 0) {
        return ''
      }
      if (!location.locationImageRelation[0].imageFk) {
        return ''
      }
      return location.locationImageRelation[0].imageFk.rendition.url
    }
  }
}
