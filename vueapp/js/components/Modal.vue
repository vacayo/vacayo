<template>
  <transition name="modal">
    <div class="modal fade show fullscreen" ref="modal" tabindex="-1" role="dialog" style="display: inherit !important;">
      <div class="modal-dialog" role="document">
        <div class="modal-content">

          <div class="modal-header">
            <slot name="header">
            </slot>
          </div>

          <div class="modal-body">
            <slot name="body">
            </slot>
          </div>

          <div class="modal-footer">
            <slot name="footer">
            </slot>
          </div>

        </div>
      </div>
    </div>
  </transition>
</template>

<script type="text/babel">
  export default {
    name: 'Modal',
    props: {
      name: String
    },
    mounted() {
      $(".modal[name='" + this.name + "']").modal('show')
    }
  }
</script>

<style>

  .modal.fullscreen .modal-dialog {
    width: 100% !important;
    max-width: 100% !important;
    height: 100% !important;
    max-height: 100% !important;
    overflow: auto !important;
    margin: 0 !important;
    padding: 0 !important;
  }

  .modal.fullscreen .modal-content {
    height: auto;
    min-height: 100%;
    border-radius: 0;
  }

  .modal.fullscreen .modal-header {
    padding: 20px 30px;
  }

  .modal.fullscreen .modal-body {
    padding: 20px 30px;
  }

  .modal.fullscreen .modal-footer {
    padding: 20px 30px;
  }

  @media (min-width: 576px) {
    .modal.fullscreen {
      padding: 80px 100px;
      background-color: currentColor;
    }
  }

  @media (min-width: 768px) {
    .modal.fullscreen {
      padding: 80px 150px;
      background-color: currentColor;
    }
  }

  @media (min-width: 992px) {
    .modal.fullscreen {
      padding: 80px 200px;
      background-color: currentColor;
    }
  }

</style>