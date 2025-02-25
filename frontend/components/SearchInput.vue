<script setup>
const props = defineProps({ texts: { required: true } });

const texts = props.texts;
const displayText = ref(""); // 타이핑 효과를 위한 span 텍스트
const inputValue = ref(""); // 사용자가 직접 입력하는 값
const currentIndex = ref(0);
const typingIndex = ref(0);
const isUserTyping = ref(false);
let timeoutId = null;

const resetTyping = () => {
  displayText.value = "";
  typingIndex.value = 0;
  currentIndex.value = 0; // 항상 처음 문장부터 시작
  clearTimeout(timeoutId);
  timeoutId = setTimeout(() => typeText(), 1500); // 500ms 대기 후 다시 시작
};

const typeText = () => {
  if (isUserTyping.value) return; // 사용자가 입력 중이면 효과 중단

  const fullText = texts[currentIndex.value];

  if (typingIndex.value < fullText.length) {
    displayText.value += fullText[typingIndex.value];
    typingIndex.value++;
    timeoutId = setTimeout(typeText, 130);
  } else {
    timeoutId = setTimeout(() => {
      displayText.value = "";
      typingIndex.value = 0;
      currentIndex.value = (currentIndex.value + 1) % texts.length;
      timeoutId = setTimeout(() => typeText(), 500); // 다음 문장 500ms 후 시작
    }, 1000);
  }
};

const handleFocus = () => {
  isUserTyping.value = true;
  displayText.value = "";
  clearTimeout(timeoutId);
};

const handleBlur = () => {
  if (!inputValue.value) {
    isUserTyping.value = false;
    resetTyping(); // 처음부터 다시 시작
  }
};

onMounted(() => {
  timeoutId = setTimeout(() => typeText(), 500); // 초기 500ms 대기 후 시작
});

onUnmounted(() => {
  clearTimeout(timeoutId);
});
</script>

<template>
  <div class="input--search">
    <div class="input-wrapper">
      <input
        v-model="inputValue"
        @focus="handleFocus"
        @blur="handleBlur"
        placeholder=""
        class="custom-input"
      />
      <span v-if="!isUserTyping && !inputValue" class="typing-effect">
        {{ displayText }}
        <span class="cursor"></span>
      </span>
    </div>
    <v-btn
      icon="mdi-arrow-right"
      variant="flat"
      color="primary"
      density="comfortable"
    ></v-btn>
  </div>
</template>

<style scoped>
.input--search {
  display: flex;
  align-items: center;
  margin-top: 2px;
}
.input--search {
  height: 58px;
  border-radius: 40px;
  padding: 4px 10px;
  border: 2px solid #d9d9d9;
  box-shadow: rgba(64, 10, 85, 0.2) 0px 2px 8px 0px;
}
.input-wrapper {
  position: relative;
  width: 100%;
}
.input-wrapper input {
  outline: none;
  padding: 0 20px 0 12px;
}
.custom-input {
  width: 100%;
  font-size: 1rem;
  outline: none;
  transition: border-color 0.3s;
  background-color: transparent;
  position: relative;
  z-index: 1;
}

.typing-effect {
  line-height: 58px;
  position: absolute;
  top: 50%;
  left: 10px;
  transform: translateY(-50%);
  font-size: 1rem;
  color: rgb(202, 202, 202);
  white-space: nowrap;
  pointer-events: none;
  z-index: 0;
}

.cursor {
  display: inline-block;
  width: 1px;
  height: 24px;
  background-color: rgb(175, 175, 175);
  margin-left: 2px;
  animation: blink 0.8s infinite;
  transform: translateY(5px);
}

.custom-input:focus + .typing-effect .cursor {
  display: none;
}

.input--search i {
  font-size: 34px;
  margin-left: 4px;
}

@keyframes blink {
  0% {
    opacity: 1;
  }
  50% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}
</style>
