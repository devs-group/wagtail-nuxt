<template>
  <div
    @click="$emit('click')"
    class="burgermenu relative w-12 h-8 cursor-pointer z-10"
  >
    <span :class="{ opened: open, animated: wasAnimated }" class="top"></span>
    <span
      :class="{ opened: open, animated: wasAnimated }"
      class="middle"
    ></span>
    <span
      :class="{ opened: open, animated: wasAnimated }"
      class="bottom"
    ></span>
  </div>
</template>

<script>
export default {
  name: 'BurgerButton',
  props: {
    open: {
      type: Boolean
    }
  },
  data() {
    return {
      wasAnimated: false
    }
  },
  watch: {
    open(value) {
      if (value) {
        this.wasAnimated = true
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.burgermenu {
  display: flex;
  flex-direction: column;
  span {
    position: absolute;
    width: 100%;
    height: 1px;
    background-color: white;
    &.top {
      top: 0;
      transform: rotateZ(0);
      &.animated {
        animation: move-back-up 0.5s;
      }
      &.opened {
        animation: move-down-and-rotate 0.5s;
        top: calc(50% - 1px);
        transform: rotateZ(45deg);
      }
    }
    &.middle {
      top: calc(50% - 1px);
      transition: opacity 0.5s ease;
      &.opened {
        opacity: 0;
      }
    }
    &.bottom {
      bottom: 1px;
      transform: rotateZ(0);
      &.animated {
        animation: move-back-down 0.5s;
      }
      &.opened {
        animation: move-up-and-rotate 0.5s;
        bottom: calc(50%);
        transform: rotateZ(-45deg);
      }
    }
  }
}
@keyframes move-up-and-rotate {
  0% {
    bottom: 1px;
    transform: rotateZ(0);
  }
  50% {
    bottom: calc(50%);
    transform: rotateZ(0);
  }
  100% {
    bottom: calc(50%);
    transform: rotateZ(-45deg);
  }
}
@keyframes move-back-down {
  0% {
    bottom: calc(50%);
    transform: rotateZ(-45deg);
  }
  50% {
    bottom: calc(50%);
    transform: rotateZ(0);
  }
  100% {
    bottom: 1px;
    transform: rotateZ(0);
  }
}
@keyframes move-down-and-rotate {
  0% {
    top: 0;
    transform: rotateZ(0);
  }
  50% {
    top: calc(50% - 1px);
    transform: rotateZ(0);
  }
  100% {
    top: calc(50% - 1px);
    transform: rotateZ(45deg);
  }
}
@keyframes move-back-up {
  0% {
    top: calc(50% - 1px);
    transform: rotateZ(45deg);
  }
  50% {
    top: calc(50% - 1px);
    transform: rotateZ(0);
  }
  100% {
    top: 0;
    transform: rotateZ(0);
  }
}
</style>
