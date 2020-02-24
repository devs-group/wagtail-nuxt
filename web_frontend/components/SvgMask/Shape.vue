<template>
  <g>
    <defs>
      <clipPath :id="clipId">
        <path :d="path" />
      </clipPath>
    </defs>
    <image
      :height="imgHeight"
      :href="imgSrc"
      :x="xOff"
      :y="yOff"
      :clip-path="`url(#${clipId})`"
    />
  </g>
</template>

<script>
export default {
  name: 'Shape',
  props: {
    clipId: {
      type: String,
      required: true
    },
    path: {
      type: String,
      required: true
    },
    xOff: {
      type: String,
      required: true
    },
    yOff: {
      type: String,
      required: true
    },
    imgSrc: {
      type: String,
      required: true
    },
    imgHeight: {
      type: String,
      required: true
    }
  }
}
</script>
