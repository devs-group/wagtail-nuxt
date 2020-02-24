<template>
  <div
    @click="$emit('click')"
    class="close-button relative w-12 h-8 cursor-pointer z-10"
  >
    <span class="top"></span>
    <span class="bottom"></span>
  </div>
</template>

<script>
export default {
  name: 'CloseButton'
}
</script>

<style lang="scss" scoped>
.close-button {
  display: flex;
  flex-direction: column;
  span {
    position: absolute;
    width: 100%;
    height: 1px;
    background-color: white;
    &.top {
      top: calc(50% - 1px);
      transform: rotateZ(45deg);
    }
    &.bottom {
      bottom: calc(50%);
      transform: rotateZ(-45deg);
    }
  }
}
</style>
