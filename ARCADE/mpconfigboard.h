#define MICROPY_HW_BOARD_NAME       "ARCADE"
#define MICROPY_HW_MCU_NAME         "STM32F401RE"
#define MICROPY_PY_SYS_PLATFORM     "Arcade"

#define MICROPY_HW_ENABLE_USB       (1)
#define MICROPY_HW_HAS_SWITCH       (1)
#define MICROPY_HW_HAS_FLASH        (1)
#define MICROPY_HW_HAS_SDCARD       (0)
#define MICROPY_HW_HAS_MMA7660      (0)
#define MICROPY_HW_HAS_LIS3DSH      (0)
#define MICROPY_HW_HAS_LCD          (0)
#define MICROPY_HW_ENABLE_RNG       (0)
#define MICROPY_HW_ENABLE_RTC       (0)
#define MICROPY_HW_ENABLE_TIMER     (1)
#define MICROPY_HW_ENABLE_SERVO     (1)
#define MICROPY_HW_ENABLE_DAC       (0)
#define MICROPY_HW_ENABLE_CAN       (0)

// HSE is 8 MHz - F401 does 84 MHz max
#define MICROPY_HW_CLK_PLLM (8)
#define MICROPY_HW_CLK_PLLN (336)
#define MICROPY_HW_CLK_PLLP (RCC_PLLP_DIV4)
#define MICROPY_HW_CLK_PLLQ (7)

#define MICROPY_HW_RTC_USE_LSE      (0)
#define MICROPY_HW_RTC_USE_US       (0)
#define MICROPY_HW_RTC_USE_CALOUT   (0)
// I2C busses
#define MICROPY_HW_I2C1_SCL (pin_B6)
#define MICROPY_HW_I2C1_SDA (pin_B7)
// SPI busses
// We don't use NSS, but need to define it.
#define MICROPY_HW_SPI1_NSS  (pin_C3)
#define MICROPY_HW_SPI1_SCK  (pin_B3)
#define MICROPY_HW_SPI1_MISO (pin_B4)
#define MICROPY_HW_SPI1_MOSI (pin_B5)

#define MICROPY_HW_SPI2_NSS  (pin_B12)
#define MICROPY_HW_SPI2_SCK  (pin_B13)
#define MICROPY_HW_SPI2_MISO (pin_B14)
#define MICROPY_HW_SPI2_MOSI (pin_B15)

// The ARCADE has only Red and Green
#define MICROPY_HW_LED1             (pin_C9)
#define MICROPY_HW_LED1_PWM         { TIM3, 3, TIM_CHANNEL_4, GPIO_AF2_TIM3 }
#define MICROPY_HW_LED_OTYPE        (GPIO_MODE_OUTPUT_PP)
#define MICROPY_HW_LED_ON(pin)      (mp_hal_pin_high(pin))
#define MICROPY_HW_LED_OFF(pin)     (mp_hal_pin_low(pin))

#define MICROPY_HW_LED2             (pin_C8)
#define MICROPY_HW_LED2_PWM         { TIM3, 3, TIM_CHANNEL_3, GPIO_AF2_TIM3 }

#define MICROPY_HW_LED3             (pin_A4)

// There are 4 switches, but the current code only supports one
// So I picked LDR0
#define MICROPY_HW_USRSW_PIN        (pin_B1)
#define MICROPY_HW_USRSW_PULL       (GPIO_PULLUP)
#define MICROPY_HW_USRSW_EXTI_MODE  (GPIO_MODE_IT_FALLING)
#define MICROPY_HW_USRSW_PRESSED    (0)

// USB config
#define MICROPY_HW_USB_FS              (1)
//#define MICROPY_HW_USB_VBUS_DETECT_PIN (pin_A9)
//#define MICROPY_HW_USB_OTG_ID_PIN      (pin_A10)

// N18 config
#define MICROPY_HW_N18_BL        (pin_C7)
#define MICROPY_HW_N18_RS        (pin_C4)
#define MICROPY_HW_N18_DC        (pin_C5)
#define MICROPY_HW_N18_CS        (pin_B12)

