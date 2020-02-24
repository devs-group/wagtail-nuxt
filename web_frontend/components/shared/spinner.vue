<template>
  <transition :name="animation">
    <div v-if="showLocally" class="spinner-wrapper">
      <div :style="`width: ${size}px; height: ${size}px`" class="spinner">
        <div class="inner"></div>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  name: 'Spinner',
  props: {
    size: {
      type: Number,
      default: 64
    },
    show: {
      type: Boolean,
      default: false
    },
    animation: {
      type: String,
      default: ''
    }
  },
  data() {
    return {
      showLocally: false
    }
  },
  watch: {
    show: {
      immediate: true,
      handler() {
        setTimeout(() => {
          this.showLocally = this.show
        }, 500)
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.spinner-wrapper {
  position: relative;
  max-height: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  .spinner {
    display: flex;
    justify-content: center;
    align-items: center;
    top: 4px;
    position: absolute;
    border-left-width: 2px;
    border-left-color: white;
    border-radius: 50%;
    animation: rotate 1s linear infinite, change-color 3s linear infinite;
    .inner {
      position: absolute;
      width: 75%;
      height: 75%;
      border-radius: 50%;
      border-right-width: 2px;
      border-right-color: white;
      animation: change-color 3s linear infinite;
    }
  }
}
@keyframes rotate {
  to {
    transform: rotate(360deg);
  }
}
@keyframes change-color {
  0% {
    opacity: 0.9;
  }
  50% {
    opacity: 0.7;
  }
  100% {
    opacity: 0.9;
  }
}
</style>
