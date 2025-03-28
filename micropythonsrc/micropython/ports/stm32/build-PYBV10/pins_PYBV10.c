// This file was automatically generated by make-pins.py
//
// --af boards/stm32f405_af.csv
// --board boards/PYBV10/pins.csv
// --prefix boards/stm32f4xx_prefix.c

// stm32f4xx_prefix.c becomes the initial portion of the generated pins file.

#include <stdio.h>

#include "py/obj.h"
#include "py/mphal.h"
#include "pin.h"

#define AF(af_idx, af_fn, af_unit, af_type, af_ptr) \
{ \
    { &pin_af_type }, \
    .name = MP_QSTR_AF ## af_idx ## _ ## af_fn ## af_unit, \
    .idx = (af_idx), \
    .fn = AF_FN_ ## af_fn, \
    .unit = (af_unit), \
    .type = AF_PIN_TYPE_ ## af_fn ## _ ## af_type, \
    .reg = (af_ptr) \
}

#define PIN(p_port, p_pin, p_af, p_adc_num, p_adc_channel) \
{ \
    { &pin_type }, \
    .name = MP_QSTR_ ## p_port ## p_pin, \
    .port = PORT_ ## p_port, \
    .pin = (p_pin), \
    .num_af = (sizeof(p_af) / sizeof(pin_af_obj_t)), \
    .pin_mask = (1 << ((p_pin) & 0x0f)), \
    .gpio = GPIO ## p_port, \
    .af = p_af, \
    .adc_num = p_adc_num, \
    .adc_channel = p_adc_channel, \
}

const pin_af_obj_t pin_A0_af[] = {
  AF( 1, TIM     ,  2, CH1       , TIM2    ), // TIM2_CH1
  AF( 1, TIM     ,  2, ETR       , TIM2    ), // TIM2_ETR
  AF( 2, TIM     ,  5, CH1       , TIM5    ), // TIM5_CH1
  AF( 3, TIM     ,  8, ETR       , TIM8    ), // TIM8_ETR
#if defined(MICROPY_HW_UART2_TX)
  AF( 7, USART   ,  2, CTS       , USART2  ), // USART2_CTS
#endif
#if defined(MICROPY_HW_UART4_TX)
  AF( 8, UART    ,  4, TX        , UART4   ), // UART4_TX
#endif
  //(11, ETH     ,  0, MII_CRS   , ETH     ), // ETH_MII_CRS
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
};

const pin_obj_t pin_A0_obj = PIN(A, 0, pin_A0_af, PIN_ADC1 | PIN_ADC2 | PIN_ADC3, 0);

const pin_af_obj_t pin_A1_af[] = {
  AF( 1, TIM     ,  2, CH2       , TIM2    ), // TIM2_CH2
  AF( 2, TIM     ,  5, CH2       , TIM5    ), // TIM5_CH2
#if defined(MICROPY_HW_UART2_TX)
  AF( 7, USART   ,  2, RTS       , USART2  ), // USART2_RTS
#endif
#if defined(MICROPY_HW_UART4_TX)
  AF( 8, UART    ,  4, RX        , UART4   ), // UART4_RX
#endif
  //(11, ETH     ,  0, MII_RX_CLK, ETH     ), // ETH_MII_RX_CLK
  //(11, ETH     ,  0, RMII_REF_CLK, ETH     ), // ETH_RMII_REF_CLK
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
};

const pin_obj_t pin_A1_obj = PIN(A, 1, pin_A1_af, PIN_ADC1 | PIN_ADC2 | PIN_ADC3, 1);

const pin_af_obj_t pin_A2_af[] = {
  AF( 1, TIM     ,  2, CH3       , TIM2    ), // TIM2_CH3
  AF( 2, TIM     ,  5, CH3       , TIM5    ), // TIM5_CH3
  AF( 3, TIM     ,  9, CH1       , TIM9    ), // TIM9_CH1
#if defined(MICROPY_HW_UART2_TX)
  AF( 7, USART   ,  2, TX        , USART2  ), // USART2_TX
#endif
  //(11, ETH     ,  0, MDIO      , ETH     ), // ETH_MDIO
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
};

const pin_obj_t pin_A2_obj = PIN(A, 2, pin_A2_af, PIN_ADC1 | PIN_ADC2 | PIN_ADC3, 2);

const pin_af_obj_t pin_A3_af[] = {
  AF( 1, TIM     ,  2, CH4       , TIM2    ), // TIM2_CH4
  AF( 2, TIM     ,  5, CH4       , TIM5    ), // TIM5_CH4
  AF( 3, TIM     ,  9, CH2       , TIM9    ), // TIM9_CH2
#if defined(MICROPY_HW_UART2_TX)
  AF( 7, USART   ,  2, RX        , USART2  ), // USART2_RX
#endif
  //(10, OTG     ,  0, HS_ULPI_D0, OTG     ), // OTG_HS_ULPI_D0
  //(11, ETH     ,  0, MII_COL   , ETH     ), // ETH_MII_COL
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
};

const pin_obj_t pin_A3_obj = PIN(A, 3, pin_A3_af, PIN_ADC1 | PIN_ADC2 | PIN_ADC3, 3);

const pin_af_obj_t pin_A4_af[] = {
#if defined(MICROPY_HW_SPI1_SCK)
  AF( 5, SPI     ,  1, NSS       , SPI1    ), // SPI1_NSS
#endif
#if defined(MICROPY_HW_SPI3_SCK)
  AF( 6, SPI     ,  3, NSS       , SPI3    ), // SPI3_NSS
#endif
#if (defined(MICROPY_HW_ENABLE_I2S3) && MICROPY_HW_ENABLE_I2S3)
  AF( 6, I2S     ,  3, WS        , I2S3    ), // I2S3_WS
#endif
#if defined(MICROPY_HW_UART2_TX)
  AF( 7, USART   ,  2, CK        , USART2  ), // USART2_CK
#endif
  //(12, OTG     ,  0, HS_SOF    , OTG     ), // OTG_HS_SOF
  //(13, DCMI    ,  0, HSYNC     , DCMI    ), // DCMI_HSYNC
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
};

const pin_obj_t pin_A4_obj = PIN(A, 4, pin_A4_af, PIN_ADC1 | PIN_ADC2, 4);

const pin_af_obj_t pin_A5_af[] = {
  AF( 1, TIM     ,  2, CH1       , TIM2    ), // TIM2_CH1
  AF( 1, TIM     ,  2, ETR       , TIM2    ), // TIM2_ETR
  AF( 3, TIM     ,  8, CH1N      , TIM8    ), // TIM8_CH1N
#if defined(MICROPY_HW_SPI1_SCK)
  AF( 5, SPI     ,  1, SCK       , SPI1    ), // SPI1_SCK
#endif
  //(10, OTG     ,  0, HS_ULPI_CK, OTG     ), // OTG_HS_ULPI_CK
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
};

const pin_obj_t pin_A5_obj = PIN(A, 5, pin_A5_af, PIN_ADC1 | PIN_ADC2, 5);

const pin_af_obj_t pin_A6_af[] = {
  AF( 1, TIM     ,  1, BKIN      , TIM1    ), // TIM1_BKIN
  AF( 2, TIM     ,  3, CH1       , TIM3    ), // TIM3_CH1
  AF( 3, TIM     ,  8, BKIN      , TIM8    ), // TIM8_BKIN
#if defined(MICROPY_HW_SPI1_SCK)
  AF( 5, SPI     ,  1, MISO      , SPI1    ), // SPI1_MISO
#endif
  AF( 9, TIM     , 13, CH1       , TIM13   ), // TIM13_CH1
  //(13, DCMI    ,  0, PIXCK     , DCMI    ), // DCMI_PIXCK
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
};

const pin_obj_t pin_A6_obj = PIN(A, 6, pin_A6_af, PIN_ADC1 | PIN_ADC2, 6);

const pin_af_obj_t pin_A7_af[] = {
  AF( 1, TIM     ,  1, CH1N      , TIM1    ), // TIM1_CH1N
  AF( 2, TIM     ,  3, CH2       , TIM3    ), // TIM3_CH2
  AF( 3, TIM     ,  8, CH1N      , TIM8    ), // TIM8_CH1N
#if defined(MICROPY_HW_SPI1_SCK)
  AF( 5, SPI     ,  1, MOSI      , SPI1    ), // SPI1_MOSI
#endif
  AF( 9, TIM     , 14, CH1       , TIM14   ), // TIM14_CH1
  //(11, ETH     ,  0, MII_RX_DV , ETH     ), // ETH_MII_RX_DV
  //(11, ETH     ,  0, RMII_CRS_DV, ETH     ), // ETH_RMII_CRS_DV
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
};

const pin_obj_t pin_A7_obj = PIN(A, 7, pin_A7_af, PIN_ADC1 | PIN_ADC2, 7);

const pin_af_obj_t pin_A8_af[] = {
  //( 0, MCO     ,  1,           , MCO1    ), // MCO1
  AF( 1, TIM     ,  1, CH1       , TIM1    ), // TIM1_CH1
#if defined(MICROPY_HW_I2C3_SCL)
  AF( 4, I2C     ,  3, SCL       , I2C3    ), // I2C3_SCL
#endif
#if defined(MICROPY_HW_UART1_TX)
  AF( 7, USART   ,  1, CK        , USART1  ), // USART1_CK
#endif
  //(10, OTG     ,  0, FS_SOF    , OTG     ), // OTG_FS_SOF
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
};

const pin_obj_t pin_A8_obj = PIN(A, 8, pin_A8_af, 0, 0);

const pin_af_obj_t pin_A9_af[] = {
  AF( 1, TIM     ,  1, CH2       , TIM1    ), // TIM1_CH2
  //( 4, I2C     ,  3, SMBA      , I2C3    ), // I2C3_SMBA
#if defined(MICROPY_HW_UART1_TX)
  AF( 7, USART   ,  1, TX        , USART1  ), // USART1_TX
#endif
  //(13, DCMI    ,  0, D0        , DCMI    ), // DCMI_D0
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
};

const pin_obj_t pin_A9_obj = PIN(A, 9, pin_A9_af, 0, 0);

const pin_af_obj_t pin_A10_af[] = {
  AF( 1, TIM     ,  1, CH3       , TIM1    ), // TIM1_CH3
#if defined(MICROPY_HW_UART1_TX)
  AF( 7, USART   ,  1, RX        , USART1  ), // USART1_RX
#endif
  //(10, OTG     ,  0, FS_ID     , OTG     ), // OTG_FS_ID
  //(13, DCMI    ,  0, D1        , DCMI    ), // DCMI_D1
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
};

const pin_obj_t pin_A10_obj = PIN(A, 10, pin_A10_af, 0, 0);

const pin_af_obj_t pin_A11_af[] = {
  AF( 1, TIM     ,  1, CH4       , TIM1    ), // TIM1_CH4
#if defined(MICROPY_HW_UART1_TX)
  AF( 7, USART   ,  1, CTS       , USART1  ), // USART1_CTS
#endif
#if defined(MICROPY_HW_CAN1_TX)
  AF( 9, CAN     ,  1, RX        , CAN1    ), // CAN1_RX
#endif
  //(10, OTG     ,  0, FS_DM     , OTG     ), // OTG_FS_DM
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
};

const pin_obj_t pin_A11_obj = PIN(A, 11, pin_A11_af, 0, 0);

const pin_af_obj_t pin_A12_af[] = {
  AF( 1, TIM     ,  1, ETR       , TIM1    ), // TIM1_ETR
#if defined(MICROPY_HW_UART1_TX)
  AF( 7, USART   ,  1, RTS       , USART1  ), // USART1_RTS
#endif
#if defined(MICROPY_HW_CAN1_TX)
  AF( 9, CAN     ,  1, TX        , CAN1    ), // CAN1_TX
#endif
  //(10, OTG     ,  0, FS_DP     , OTG     ), // OTG_FS_DP
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
};

const pin_obj_t pin_A12_obj = PIN(A, 12, pin_A12_af, 0, 0);

// const pin_af_obj_t pin_A13_af[] = {
  //( 0, JTMS    ,  0,           , JTMS    ), // JTMS
  //( 0, SWDIO   ,  0,           , SWDIO   ), // SWDIO
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
// };

const pin_obj_t pin_A13_obj = PIN(A, 13, NULL, 0, 0);

// const pin_af_obj_t pin_A14_af[] = {
  //( 0, JTCK    ,  0,           , JTCK    ), // JTCK
  //( 0, SWCLK   ,  0,           , SWCLK   ), // SWCLK
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
// };

const pin_obj_t pin_A14_obj = PIN(A, 14, NULL, 0, 0);

const pin_af_obj_t pin_A15_af[] = {
  //( 0, JTDI    ,  0,           , JTDI    ), // JTDI
  AF( 1, TIM     ,  2, CH1       , TIM2    ), // TIM2_CH1
  AF( 1, TIM     ,  2, ETR       , TIM2    ), // TIM2_ETR
#if defined(MICROPY_HW_SPI1_SCK)
  AF( 5, SPI     ,  1, NSS       , SPI1    ), // SPI1_NSS
#endif
#if defined(MICROPY_HW_SPI3_SCK)
  AF( 6, SPI     ,  3, NSS       , SPI3    ), // SPI3_NSS
#endif
#if (defined(MICROPY_HW_ENABLE_I2S3) && MICROPY_HW_ENABLE_I2S3)
  AF( 6, I2S     ,  3, WS        , I2S3    ), // I2S3_WS
#endif
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
};

const pin_obj_t pin_A15_obj = PIN(A, 15, pin_A15_af, 0, 0);

const pin_af_obj_t pin_B0_af[] = {
  AF( 1, TIM     ,  1, CH2N      , TIM1    ), // TIM1_CH2N
  AF( 2, TIM     ,  3, CH3       , TIM3    ), // TIM3_CH3
  AF( 3, TIM     ,  8, CH2N      , TIM8    ), // TIM8_CH2N
  //(10, OTG     ,  0, HS_ULPI_D1, OTG     ), // OTG_HS_ULPI_D1
  //(11, ETH     ,  0, MII_RXD2  , ETH     ), // ETH_MII_RXD2
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
};

const pin_obj_t pin_B0_obj = PIN(B, 0, pin_B0_af, PIN_ADC1 | PIN_ADC2, 8);

const pin_af_obj_t pin_B1_af[] = {
  AF( 1, TIM     ,  1, CH3N      , TIM1    ), // TIM1_CH3N
  AF( 2, TIM     ,  3, CH4       , TIM3    ), // TIM3_CH4
  AF( 3, TIM     ,  8, CH3N      , TIM8    ), // TIM8_CH3N
  //(10, OTG     ,  0, HS_ULPI_D2, OTG     ), // OTG_HS_ULPI_D2
  //(11, ETH     ,  0, MII_RXD3  , ETH     ), // ETH_MII_RXD3
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
};

const pin_obj_t pin_B1_obj = PIN(B, 1, pin_B1_af, PIN_ADC1 | PIN_ADC2, 9);

// const pin_af_obj_t pin_B2_af[] = {
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
// };

const pin_obj_t pin_B2_obj = PIN(B, 2, NULL, 0, 0);

const pin_af_obj_t pin_B3_af[] = {
  //( 0, JTDO    ,  0,           , JTDO    ), // JTDO
  //( 0, TRACESWO,  0,           , TRACESWO), // TRACESWO
  AF( 1, TIM     ,  2, CH2       , TIM2    ), // TIM2_CH2
#if defined(MICROPY_HW_SPI1_SCK)
  AF( 5, SPI     ,  1, SCK       , SPI1    ), // SPI1_SCK
#endif
#if defined(MICROPY_HW_SPI3_SCK)
  AF( 6, SPI     ,  3, SCK       , SPI3    ), // SPI3_SCK
#endif
#if (defined(MICROPY_HW_ENABLE_I2S3) && MICROPY_HW_ENABLE_I2S3)
  AF( 6, I2S     ,  3, CK        , I2S3    ), // I2S3_CK
#endif
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
};

const pin_obj_t pin_B3_obj = PIN(B, 3, pin_B3_af, 0, 0);

const pin_af_obj_t pin_B4_af[] = {
  //( 0, NJTRST  ,  0,           , NJTRST  ), // NJTRST
  AF( 2, TIM     ,  3, CH1       , TIM3    ), // TIM3_CH1
#if defined(MICROPY_HW_SPI1_SCK)
  AF( 5, SPI     ,  1, MISO      , SPI1    ), // SPI1_MISO
#endif
#if defined(MICROPY_HW_SPI3_SCK)
  AF( 6, SPI     ,  3, MISO      , SPI3    ), // SPI3_MISO
#endif
#if (defined(MICROPY_HW_ENABLE_I2S3) && MICROPY_HW_ENABLE_I2S3)
  AF( 7, I2S     ,  3, EXTSD     , I2S3    ), // I2S3_EXTSD
#endif
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
};

const pin_obj_t pin_B4_obj = PIN(B, 4, pin_B4_af, 0, 0);

const pin_af_obj_t pin_B5_af[] = {
  AF( 2, TIM     ,  3, CH2       , TIM3    ), // TIM3_CH2
  //( 4, I2C     ,  1, SMBA      , I2C1    ), // I2C1_SMBA
#if defined(MICROPY_HW_SPI1_SCK)
  AF( 5, SPI     ,  1, MOSI      , SPI1    ), // SPI1_MOSI
#endif
#if defined(MICROPY_HW_SPI3_SCK)
  AF( 6, SPI     ,  3, MOSI      , SPI3    ), // SPI3_MOSI
#endif
#if (defined(MICROPY_HW_ENABLE_I2S3) && MICROPY_HW_ENABLE_I2S3)
  AF( 6, I2S     ,  3, SD        , I2S3    ), // I2S3_SD
#endif
#if defined(MICROPY_HW_CAN2_TX)
  AF( 9, CAN     ,  2, RX        , CAN2    ), // CAN2_RX
#endif
  //(10, OTG     ,  0, HS_ULPI_D7, OTG     ), // OTG_HS_ULPI_D7
  //(11, ETH     ,  0, PPS_OUT   , ETH     ), // ETH_PPS_OUT
  //(13, DCMI    ,  0, D10       , DCMI    ), // DCMI_D10
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
};

const pin_obj_t pin_B5_obj = PIN(B, 5, pin_B5_af, 0, 0);

const pin_af_obj_t pin_B6_af[] = {
  AF( 2, TIM     ,  4, CH1       , TIM4    ), // TIM4_CH1
#if defined(MICROPY_HW_I2C1_SCL)
  AF( 4, I2C     ,  1, SCL       , I2C1    ), // I2C1_SCL
#endif
#if defined(MICROPY_HW_UART1_TX)
  AF( 7, USART   ,  1, TX        , USART1  ), // USART1_TX
#endif
#if defined(MICROPY_HW_CAN2_TX)
  AF( 9, CAN     ,  2, TX        , CAN2    ), // CAN2_TX
#endif
  //(13, DCMI    ,  0, D5        , DCMI    ), // DCMI_D5
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
};

const pin_obj_t pin_B6_obj = PIN(B, 6, pin_B6_af, 0, 0);

const pin_af_obj_t pin_B7_af[] = {
  AF( 2, TIM     ,  4, CH2       , TIM4    ), // TIM4_CH2
#if defined(MICROPY_HW_I2C1_SCL)
  AF( 4, I2C     ,  1, SDA       , I2C1    ), // I2C1_SDA
#endif
#if defined(MICROPY_HW_UART1_TX)
  AF( 7, USART   ,  1, RX        , USART1  ), // USART1_RX
#endif
  //(12, FSMC    ,  0, NL        , FSMC    ), // FSMC_NL
  //(13, DCMI    ,  0, VSYNC     , DCMI    ), // DCMI_VSYNC
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
};

const pin_obj_t pin_B7_obj = PIN(B, 7, pin_B7_af, 0, 0);

const pin_af_obj_t pin_B8_af[] = {
  AF( 2, TIM     ,  4, CH3       , TIM4    ), // TIM4_CH3
  AF( 3, TIM     , 10, CH1       , TIM10   ), // TIM10_CH1
#if defined(MICROPY_HW_I2C1_SCL)
  AF( 4, I2C     ,  1, SCL       , I2C1    ), // I2C1_SCL
#endif
#if defined(MICROPY_HW_CAN1_TX)
  AF( 9, CAN     ,  1, RX        , CAN1    ), // CAN1_RX
#endif
  //(11, ETH     ,  0, MII_TXD3  , ETH     ), // ETH_MII_TXD3
  //(12, SDIO    ,  0, D4        , SDIO    ), // SDIO_D4
  //(13, DCMI    ,  0, D6        , DCMI    ), // DCMI_D6
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
};

const pin_obj_t pin_B8_obj = PIN(B, 8, pin_B8_af, 0, 0);

const pin_af_obj_t pin_B9_af[] = {
  AF( 2, TIM     ,  4, CH4       , TIM4    ), // TIM4_CH4
  AF( 3, TIM     , 11, CH1       , TIM11   ), // TIM11_CH1
#if defined(MICROPY_HW_I2C1_SCL)
  AF( 4, I2C     ,  1, SDA       , I2C1    ), // I2C1_SDA
#endif
#if defined(MICROPY_HW_SPI2_SCK)
  AF( 5, SPI     ,  2, NSS       , SPI2    ), // SPI2_NSS
#endif
#if (defined(MICROPY_HW_ENABLE_I2S2) && MICROPY_HW_ENABLE_I2S2)
  AF( 5, I2S     ,  2, WS        , I2S2    ), // I2S2_WS
#endif
#if defined(MICROPY_HW_CAN1_TX)
  AF( 9, CAN     ,  1, TX        , CAN1    ), // CAN1_TX
#endif
  //(12, SDIO    ,  0, D5        , SDIO    ), // SDIO_D5
  //(13, DCMI    ,  0, D7        , DCMI    ), // DCMI_D7
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
};

const pin_obj_t pin_B9_obj = PIN(B, 9, pin_B9_af, 0, 0);

const pin_af_obj_t pin_B10_af[] = {
  AF( 1, TIM     ,  2, CH3       , TIM2    ), // TIM2_CH3
#if defined(MICROPY_HW_I2C2_SCL)
  AF( 4, I2C     ,  2, SCL       , I2C2    ), // I2C2_SCL
#endif
#if defined(MICROPY_HW_SPI2_SCK)
  AF( 5, SPI     ,  2, SCK       , SPI2    ), // SPI2_SCK
#endif
#if (defined(MICROPY_HW_ENABLE_I2S2) && MICROPY_HW_ENABLE_I2S2)
  AF( 5, I2S     ,  2, CK        , I2S2    ), // I2S2_CK
#endif
#if defined(MICROPY_HW_UART3_TX)
  AF( 7, USART   ,  3, TX        , USART3  ), // USART3_TX
#endif
  //(10, OTG     ,  0, HS_ULPI_D3, OTG     ), // OTG_HS_ULPI_D3
  //(11, ETH     ,  0, MII_RX_ER , ETH     ), // ETH_MII_RX_ER
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
};

const pin_obj_t pin_B10_obj = PIN(B, 10, pin_B10_af, 0, 0);

const pin_af_obj_t pin_B11_af[] = {
  AF( 1, TIM     ,  2, CH4       , TIM2    ), // TIM2_CH4
#if defined(MICROPY_HW_I2C2_SCL)
  AF( 4, I2C     ,  2, SDA       , I2C2    ), // I2C2_SDA
#endif
#if defined(MICROPY_HW_UART3_TX)
  AF( 7, USART   ,  3, RX        , USART3  ), // USART3_RX
#endif
  //(10, OTG     ,  0, HS_ULPI_D4, OTG     ), // OTG_HS_ULPI_D4
  //(11, ETH     ,  0, MII_TX_EN , ETH     ), // ETH_MII_TX_EN
  //(11, ETH     ,  0, RMII_TX_EN, ETH     ), // ETH_RMII_TX_EN
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
};

const pin_obj_t pin_B11_obj = PIN(B, 11, pin_B11_af, 0, 0);

const pin_af_obj_t pin_B12_af[] = {
  AF( 1, TIM     ,  1, BKIN      , TIM1    ), // TIM1_BKIN
  //( 4, I2C     ,  2, SMBA      , I2C2    ), // I2C2_SMBA
#if defined(MICROPY_HW_SPI2_SCK)
  AF( 5, SPI     ,  2, NSS       , SPI2    ), // SPI2_NSS
#endif
#if (defined(MICROPY_HW_ENABLE_I2S2) && MICROPY_HW_ENABLE_I2S2)
  AF( 5, I2S     ,  2, WS        , I2S2    ), // I2S2_WS
#endif
#if defined(MICROPY_HW_UART3_TX)
  AF( 7, USART   ,  3, CK        , USART3  ), // USART3_CK
#endif
#if defined(MICROPY_HW_CAN2_TX)
  AF( 9, CAN     ,  2, RX        , CAN2    ), // CAN2_RX
#endif
  //(10, OTG     ,  0, HS_ULPI_D5, OTG     ), // OTG_HS_ULPI_D5
  //(11, ETH     ,  0, MII_TXD0  , ETH     ), // ETH_MII_TXD0
  //(11, ETH     ,  0, RMII_TXD0 , ETH     ), // ETH_RMII_TXD0
  //(12, OTG     ,  0, HS_ID     , OTG     ), // OTG_HS_ID
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
};

const pin_obj_t pin_B12_obj = PIN(B, 12, pin_B12_af, 0, 0);

const pin_af_obj_t pin_B13_af[] = {
  AF( 1, TIM     ,  1, CH1N      , TIM1    ), // TIM1_CH1N
#if defined(MICROPY_HW_SPI2_SCK)
  AF( 5, SPI     ,  2, SCK       , SPI2    ), // SPI2_SCK
#endif
#if (defined(MICROPY_HW_ENABLE_I2S2) && MICROPY_HW_ENABLE_I2S2)
  AF( 5, I2S     ,  2, CK        , I2S2    ), // I2S2_CK
#endif
#if defined(MICROPY_HW_UART3_TX)
  AF( 7, USART   ,  3, CTS       , USART3  ), // USART3_CTS
#endif
#if defined(MICROPY_HW_CAN2_TX)
  AF( 9, CAN     ,  2, TX        , CAN2    ), // CAN2_TX
#endif
  //(10, OTG     ,  0, HS_ULPI_D6, OTG     ), // OTG_HS_ULPI_D6
  //(11, ETH     ,  0, MII_TXD1  , ETH     ), // ETH_MII_TXD1
  //(11, ETH     ,  0, RMII_TXD1 , ETH     ), // ETH_RMII_TXD1
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
};

const pin_obj_t pin_B13_obj = PIN(B, 13, pin_B13_af, 0, 0);

const pin_af_obj_t pin_B14_af[] = {
  AF( 1, TIM     ,  1, CH2N      , TIM1    ), // TIM1_CH2N
  AF( 3, TIM     ,  8, CH2N      , TIM8    ), // TIM8_CH2N
#if defined(MICROPY_HW_SPI2_SCK)
  AF( 5, SPI     ,  2, MISO      , SPI2    ), // SPI2_MISO
#endif
#if (defined(MICROPY_HW_ENABLE_I2S2) && MICROPY_HW_ENABLE_I2S2)
  AF( 6, I2S     ,  2, EXTSD     , I2S2    ), // I2S2_EXTSD
#endif
#if defined(MICROPY_HW_UART3_TX)
  AF( 7, USART   ,  3, RTS       , USART3  ), // USART3_RTS
#endif
  AF( 9, TIM     , 12, CH1       , TIM12   ), // TIM12_CH1
  //(12, OTG     ,  0, HS_DM     , OTG     ), // OTG_HS_DM
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
};

const pin_obj_t pin_B14_obj = PIN(B, 14, pin_B14_af, 0, 0);

const pin_af_obj_t pin_B15_af[] = {
  //( 0, RTC     ,  0, REFIN     , RTC     ), // RTC_REFIN
  AF( 1, TIM     ,  1, CH3N      , TIM1    ), // TIM1_CH3N
  AF( 3, TIM     ,  8, CH3N      , TIM8    ), // TIM8_CH3N
#if defined(MICROPY_HW_SPI2_SCK)
  AF( 5, SPI     ,  2, MOSI      , SPI2    ), // SPI2_MOSI
#endif
#if (defined(MICROPY_HW_ENABLE_I2S2) && MICROPY_HW_ENABLE_I2S2)
  AF( 5, I2S     ,  2, SD        , I2S2    ), // I2S2_SD
#endif
  AF( 9, TIM     , 12, CH2       , TIM12   ), // TIM12_CH2
  //(12, OTG     ,  0, HS_DP     , OTG     ), // OTG_HS_DP
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
};

const pin_obj_t pin_B15_obj = PIN(B, 15, pin_B15_af, 0, 0);

// const pin_af_obj_t pin_C0_af[] = {
  //(10, OTG     ,  0, HS_ULPI_STP, OTG     ), // OTG_HS_ULPI_STP
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
// };

const pin_obj_t pin_C0_obj = PIN(C, 0, NULL, PIN_ADC1 | PIN_ADC2 | PIN_ADC3, 10);

// const pin_af_obj_t pin_C1_af[] = {
  //(11, ETH     ,  0, MDC       , ETH     ), // ETH_MDC
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
// };

const pin_obj_t pin_C1_obj = PIN(C, 1, NULL, PIN_ADC1 | PIN_ADC2 | PIN_ADC3, 11);

const pin_af_obj_t pin_C2_af[] = {
#if defined(MICROPY_HW_SPI2_SCK)
  AF( 5, SPI     ,  2, MISO      , SPI2    ), // SPI2_MISO
#endif
#if (defined(MICROPY_HW_ENABLE_I2S2) && MICROPY_HW_ENABLE_I2S2)
  AF( 6, I2S     ,  2, EXTSD     , I2S2    ), // I2S2_EXTSD
#endif
  //(10, OTG     ,  0, HS_ULPI_DIR, OTG     ), // OTG_HS_ULPI_DIR
  //(11, ETH     ,  0, MII_TXD2  , ETH     ), // ETH_MII_TXD2
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
};

const pin_obj_t pin_C2_obj = PIN(C, 2, pin_C2_af, PIN_ADC1 | PIN_ADC2 | PIN_ADC3, 12);

const pin_af_obj_t pin_C3_af[] = {
#if defined(MICROPY_HW_SPI2_SCK)
  AF( 5, SPI     ,  2, MOSI      , SPI2    ), // SPI2_MOSI
#endif
#if (defined(MICROPY_HW_ENABLE_I2S2) && MICROPY_HW_ENABLE_I2S2)
  AF( 5, I2S     ,  2, SD        , I2S2    ), // I2S2_SD
#endif
  //(10, OTG     ,  0, HS_ULPI_NXT, OTG     ), // OTG_HS_ULPI_NXT
  //(11, ETH     ,  0, MII_TX_CLK, ETH     ), // ETH_MII_TX_CLK
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
};

const pin_obj_t pin_C3_obj = PIN(C, 3, pin_C3_af, PIN_ADC1 | PIN_ADC2 | PIN_ADC3, 13);

// const pin_af_obj_t pin_C4_af[] = {
  //(11, ETH     ,  0, MII_RXD0  , ETH     ), // ETH_MII_RXD0
  //(11, ETH     ,  0, RMII_RXD0 , ETH     ), // ETH_RMII_RXD0
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
// };

const pin_obj_t pin_C4_obj = PIN(C, 4, NULL, PIN_ADC1 | PIN_ADC2 | PIN_ADC3, 14);

// const pin_af_obj_t pin_C5_af[] = {
  //(11, ETH     ,  0, MII_RXD1  , ETH     ), // ETH_MII_RXD1
  //(11, ETH     ,  0, RMII_RXD1 , ETH     ), // ETH_RMII_RXD1
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
// };

const pin_obj_t pin_C5_obj = PIN(C, 5, NULL, PIN_ADC1 | PIN_ADC2 | PIN_ADC3, 15);

const pin_af_obj_t pin_C6_af[] = {
  AF( 2, TIM     ,  3, CH1       , TIM3    ), // TIM3_CH1
  AF( 3, TIM     ,  8, CH1       , TIM8    ), // TIM8_CH1
#if (defined(MICROPY_HW_ENABLE_I2S2) && MICROPY_HW_ENABLE_I2S2)
  AF( 5, I2S     ,  2, MCK       , I2S2    ), // I2S2_MCK
#endif
#if defined(MICROPY_HW_UART6_TX)
  AF( 8, USART   ,  6, TX        , USART6  ), // USART6_TX
#endif
  //(12, SDIO    ,  0, D6        , SDIO    ), // SDIO_D6
  //(13, DCMI    ,  0, D0        , DCMI    ), // DCMI_D0
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
};

const pin_obj_t pin_C6_obj = PIN(C, 6, pin_C6_af, 0, 0);

const pin_af_obj_t pin_C7_af[] = {
  AF( 2, TIM     ,  3, CH2       , TIM3    ), // TIM3_CH2
  AF( 3, TIM     ,  8, CH2       , TIM8    ), // TIM8_CH2
#if (defined(MICROPY_HW_ENABLE_I2S3) && MICROPY_HW_ENABLE_I2S3)
  AF( 6, I2S     ,  3, MCK       , I2S3    ), // I2S3_MCK
#endif
#if defined(MICROPY_HW_UART6_TX)
  AF( 8, USART   ,  6, RX        , USART6  ), // USART6_RX
#endif
  //(12, SDIO    ,  0, D7        , SDIO    ), // SDIO_D7
  //(13, DCMI    ,  0, D1        , DCMI    ), // DCMI_D1
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
};

const pin_obj_t pin_C7_obj = PIN(C, 7, pin_C7_af, 0, 0);

const pin_af_obj_t pin_C8_af[] = {
  AF( 2, TIM     ,  3, CH3       , TIM3    ), // TIM3_CH3
  AF( 3, TIM     ,  8, CH3       , TIM8    ), // TIM8_CH3
#if defined(MICROPY_HW_UART6_TX)
  AF( 8, USART   ,  6, CK        , USART6  ), // USART6_CK
#endif
  //(12, SDIO    ,  0, D0        , SDIO    ), // SDIO_D0
  //(13, DCMI    ,  0, D2        , DCMI    ), // DCMI_D2
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
};

const pin_obj_t pin_C8_obj = PIN(C, 8, pin_C8_af, 0, 0);

const pin_af_obj_t pin_C9_af[] = {
  //( 0, MCO     ,  2,           , MCO2    ), // MCO2
  AF( 2, TIM     ,  3, CH4       , TIM3    ), // TIM3_CH4
  AF( 3, TIM     ,  8, CH4       , TIM8    ), // TIM8_CH4
#if defined(MICROPY_HW_I2C3_SCL)
  AF( 4, I2C     ,  3, SDA       , I2C3    ), // I2C3_SDA
#endif
  //( 5, I2S     ,  0, CKIN      , I2S     ), // I2S_CKIN
  //(12, SDIO    ,  0, D1        , SDIO    ), // SDIO_D1
  //(13, DCMI    ,  0, D3        , DCMI    ), // DCMI_D3
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
};

const pin_obj_t pin_C9_obj = PIN(C, 9, pin_C9_af, 0, 0);

const pin_af_obj_t pin_C10_af[] = {
#if defined(MICROPY_HW_SPI3_SCK)
  AF( 6, SPI     ,  3, SCK       , SPI3    ), // SPI3_SCK
#endif
#if (defined(MICROPY_HW_ENABLE_I2S3) && MICROPY_HW_ENABLE_I2S3)
  AF( 6, I2S     ,  3, CK        , I2S3    ), // I2S3_CK
#endif
#if defined(MICROPY_HW_UART3_TX)
  AF( 7, USART   ,  3, TX        , USART3  ), // USART3_TX
#endif
#if defined(MICROPY_HW_UART4_TX)
  AF( 8, UART    ,  4, TX        , UART4   ), // UART4_TX
#endif
  //(12, SDIO    ,  0, D2        , SDIO    ), // SDIO_D2
  //(13, DCMI    ,  0, D8        , DCMI    ), // DCMI_D8
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
};

const pin_obj_t pin_C10_obj = PIN(C, 10, pin_C10_af, 0, 0);

const pin_af_obj_t pin_C11_af[] = {
#if (defined(MICROPY_HW_ENABLE_I2S3) && MICROPY_HW_ENABLE_I2S3)
  AF( 5, I2S     ,  3, EXTSD     , I2S3    ), // I2S3_EXTSD
#endif
#if defined(MICROPY_HW_SPI3_SCK)
  AF( 6, SPI     ,  3, MISO      , SPI3    ), // SPI3_MISO
#endif
#if defined(MICROPY_HW_UART3_TX)
  AF( 7, USART   ,  3, RX        , USART3  ), // USART3_RX
#endif
#if defined(MICROPY_HW_UART4_TX)
  AF( 8, UART    ,  4, RX        , UART4   ), // UART4_RX
#endif
  //(12, SDIO    ,  0, D3        , SDIO    ), // SDIO_D3
  //(13, DCMI    ,  0, D4        , DCMI    ), // DCMI_D4
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
};

const pin_obj_t pin_C11_obj = PIN(C, 11, pin_C11_af, 0, 0);

const pin_af_obj_t pin_C12_af[] = {
#if defined(MICROPY_HW_SPI3_SCK)
  AF( 6, SPI     ,  3, MOSI      , SPI3    ), // SPI3_MOSI
#endif
#if (defined(MICROPY_HW_ENABLE_I2S3) && MICROPY_HW_ENABLE_I2S3)
  AF( 6, I2S     ,  3, SD        , I2S3    ), // I2S3_SD
#endif
#if defined(MICROPY_HW_UART3_TX)
  AF( 7, USART   ,  3, CK        , USART3  ), // USART3_CK
#endif
#if defined(MICROPY_HW_UART5_TX)
  AF( 8, UART    ,  5, TX        , UART5   ), // UART5_TX
#endif
  //(12, SDIO    ,  0, CK        , SDIO    ), // SDIO_CK
  //(13, DCMI    ,  0, D9        , DCMI    ), // DCMI_D9
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
};

const pin_obj_t pin_C12_obj = PIN(C, 12, pin_C12_af, 0, 0);

// const pin_af_obj_t pin_C13_af[] = {
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
// };

const pin_obj_t pin_C13_obj = PIN(C, 13, NULL, 0, 0);

const pin_af_obj_t pin_D2_af[] = {
  AF( 2, TIM     ,  3, ETR       , TIM3    ), // TIM3_ETR
#if defined(MICROPY_HW_UART5_TX)
  AF( 8, UART    ,  5, RX        , UART5   ), // UART5_RX
#endif
  //(12, SDIO    ,  0, CMD       , SDIO    ), // SDIO_CMD
  //(13, DCMI    ,  0, D11       , DCMI    ), // DCMI_D11
  //(15, EVENTOUT,  0,           , EVENTOUT), // EVENTOUT
};

const pin_obj_t pin_D2_obj = PIN(D, 2, pin_D2_af, 0, 0);

STATIC const mp_rom_map_elem_t pin_cpu_pins_locals_dict_table[] = {
  { MP_ROM_QSTR(MP_QSTR_A0), MP_ROM_PTR(&pin_A0_obj) },
  { MP_ROM_QSTR(MP_QSTR_A1), MP_ROM_PTR(&pin_A1_obj) },
  { MP_ROM_QSTR(MP_QSTR_A2), MP_ROM_PTR(&pin_A2_obj) },
  { MP_ROM_QSTR(MP_QSTR_A3), MP_ROM_PTR(&pin_A3_obj) },
  { MP_ROM_QSTR(MP_QSTR_A4), MP_ROM_PTR(&pin_A4_obj) },
  { MP_ROM_QSTR(MP_QSTR_A5), MP_ROM_PTR(&pin_A5_obj) },
  { MP_ROM_QSTR(MP_QSTR_A6), MP_ROM_PTR(&pin_A6_obj) },
  { MP_ROM_QSTR(MP_QSTR_A7), MP_ROM_PTR(&pin_A7_obj) },
  { MP_ROM_QSTR(MP_QSTR_A8), MP_ROM_PTR(&pin_A8_obj) },
  { MP_ROM_QSTR(MP_QSTR_A9), MP_ROM_PTR(&pin_A9_obj) },
  { MP_ROM_QSTR(MP_QSTR_A10), MP_ROM_PTR(&pin_A10_obj) },
  { MP_ROM_QSTR(MP_QSTR_A11), MP_ROM_PTR(&pin_A11_obj) },
  { MP_ROM_QSTR(MP_QSTR_A12), MP_ROM_PTR(&pin_A12_obj) },
  { MP_ROM_QSTR(MP_QSTR_A13), MP_ROM_PTR(&pin_A13_obj) },
  { MP_ROM_QSTR(MP_QSTR_A14), MP_ROM_PTR(&pin_A14_obj) },
  { MP_ROM_QSTR(MP_QSTR_A15), MP_ROM_PTR(&pin_A15_obj) },
  { MP_ROM_QSTR(MP_QSTR_B0), MP_ROM_PTR(&pin_B0_obj) },
  { MP_ROM_QSTR(MP_QSTR_B1), MP_ROM_PTR(&pin_B1_obj) },
  { MP_ROM_QSTR(MP_QSTR_B2), MP_ROM_PTR(&pin_B2_obj) },
  { MP_ROM_QSTR(MP_QSTR_B3), MP_ROM_PTR(&pin_B3_obj) },
  { MP_ROM_QSTR(MP_QSTR_B4), MP_ROM_PTR(&pin_B4_obj) },
  { MP_ROM_QSTR(MP_QSTR_B5), MP_ROM_PTR(&pin_B5_obj) },
  { MP_ROM_QSTR(MP_QSTR_B6), MP_ROM_PTR(&pin_B6_obj) },
  { MP_ROM_QSTR(MP_QSTR_B7), MP_ROM_PTR(&pin_B7_obj) },
  { MP_ROM_QSTR(MP_QSTR_B8), MP_ROM_PTR(&pin_B8_obj) },
  { MP_ROM_QSTR(MP_QSTR_B9), MP_ROM_PTR(&pin_B9_obj) },
  { MP_ROM_QSTR(MP_QSTR_B10), MP_ROM_PTR(&pin_B10_obj) },
  { MP_ROM_QSTR(MP_QSTR_B11), MP_ROM_PTR(&pin_B11_obj) },
  { MP_ROM_QSTR(MP_QSTR_B12), MP_ROM_PTR(&pin_B12_obj) },
  { MP_ROM_QSTR(MP_QSTR_B13), MP_ROM_PTR(&pin_B13_obj) },
  { MP_ROM_QSTR(MP_QSTR_B14), MP_ROM_PTR(&pin_B14_obj) },
  { MP_ROM_QSTR(MP_QSTR_B15), MP_ROM_PTR(&pin_B15_obj) },
  { MP_ROM_QSTR(MP_QSTR_C0), MP_ROM_PTR(&pin_C0_obj) },
  { MP_ROM_QSTR(MP_QSTR_C1), MP_ROM_PTR(&pin_C1_obj) },
  { MP_ROM_QSTR(MP_QSTR_C2), MP_ROM_PTR(&pin_C2_obj) },
  { MP_ROM_QSTR(MP_QSTR_C3), MP_ROM_PTR(&pin_C3_obj) },
  { MP_ROM_QSTR(MP_QSTR_C4), MP_ROM_PTR(&pin_C4_obj) },
  { MP_ROM_QSTR(MP_QSTR_C5), MP_ROM_PTR(&pin_C5_obj) },
  { MP_ROM_QSTR(MP_QSTR_C6), MP_ROM_PTR(&pin_C6_obj) },
  { MP_ROM_QSTR(MP_QSTR_C7), MP_ROM_PTR(&pin_C7_obj) },
  { MP_ROM_QSTR(MP_QSTR_C8), MP_ROM_PTR(&pin_C8_obj) },
  { MP_ROM_QSTR(MP_QSTR_C9), MP_ROM_PTR(&pin_C9_obj) },
  { MP_ROM_QSTR(MP_QSTR_C10), MP_ROM_PTR(&pin_C10_obj) },
  { MP_ROM_QSTR(MP_QSTR_C11), MP_ROM_PTR(&pin_C11_obj) },
  { MP_ROM_QSTR(MP_QSTR_C12), MP_ROM_PTR(&pin_C12_obj) },
  { MP_ROM_QSTR(MP_QSTR_C13), MP_ROM_PTR(&pin_C13_obj) },
  { MP_ROM_QSTR(MP_QSTR_D2), MP_ROM_PTR(&pin_D2_obj) },
};
MP_DEFINE_CONST_DICT(pin_cpu_pins_locals_dict, pin_cpu_pins_locals_dict_table);

STATIC const mp_rom_map_elem_t pin_board_pins_locals_dict_table[] = {
  { MP_ROM_QSTR(MP_QSTR_X1), MP_ROM_PTR(&pin_A0_obj) },
  { MP_ROM_QSTR(MP_QSTR_X2), MP_ROM_PTR(&pin_A1_obj) },
  { MP_ROM_QSTR(MP_QSTR_X3), MP_ROM_PTR(&pin_A2_obj) },
  { MP_ROM_QSTR(MP_QSTR_X4), MP_ROM_PTR(&pin_A3_obj) },
  { MP_ROM_QSTR(MP_QSTR_X5), MP_ROM_PTR(&pin_A4_obj) },
  { MP_ROM_QSTR(MP_QSTR_X6), MP_ROM_PTR(&pin_A5_obj) },
  { MP_ROM_QSTR(MP_QSTR_X7), MP_ROM_PTR(&pin_A6_obj) },
  { MP_ROM_QSTR(MP_QSTR_X8), MP_ROM_PTR(&pin_A7_obj) },
  { MP_ROM_QSTR(MP_QSTR_X9), MP_ROM_PTR(&pin_B6_obj) },
  { MP_ROM_QSTR(MP_QSTR_X10), MP_ROM_PTR(&pin_B7_obj) },
  { MP_ROM_QSTR(MP_QSTR_X11), MP_ROM_PTR(&pin_C4_obj) },
  { MP_ROM_QSTR(MP_QSTR_X12), MP_ROM_PTR(&pin_C5_obj) },
  { MP_ROM_QSTR(MP_QSTR_X17), MP_ROM_PTR(&pin_B3_obj) },
  { MP_ROM_QSTR(MP_QSTR_X18), MP_ROM_PTR(&pin_C13_obj) },
  { MP_ROM_QSTR(MP_QSTR_X19), MP_ROM_PTR(&pin_C0_obj) },
  { MP_ROM_QSTR(MP_QSTR_X20), MP_ROM_PTR(&pin_C1_obj) },
  { MP_ROM_QSTR(MP_QSTR_X21), MP_ROM_PTR(&pin_C2_obj) },
  { MP_ROM_QSTR(MP_QSTR_X22), MP_ROM_PTR(&pin_C3_obj) },
  { MP_ROM_QSTR(MP_QSTR_Y1), MP_ROM_PTR(&pin_C6_obj) },
  { MP_ROM_QSTR(MP_QSTR_Y2), MP_ROM_PTR(&pin_C7_obj) },
  { MP_ROM_QSTR(MP_QSTR_Y3), MP_ROM_PTR(&pin_B8_obj) },
  { MP_ROM_QSTR(MP_QSTR_Y4), MP_ROM_PTR(&pin_B9_obj) },
  { MP_ROM_QSTR(MP_QSTR_Y5), MP_ROM_PTR(&pin_B12_obj) },
  { MP_ROM_QSTR(MP_QSTR_Y6), MP_ROM_PTR(&pin_B13_obj) },
  { MP_ROM_QSTR(MP_QSTR_Y7), MP_ROM_PTR(&pin_B14_obj) },
  { MP_ROM_QSTR(MP_QSTR_Y8), MP_ROM_PTR(&pin_B15_obj) },
  { MP_ROM_QSTR(MP_QSTR_Y9), MP_ROM_PTR(&pin_B10_obj) },
  { MP_ROM_QSTR(MP_QSTR_Y10), MP_ROM_PTR(&pin_B11_obj) },
  { MP_ROM_QSTR(MP_QSTR_Y11), MP_ROM_PTR(&pin_B0_obj) },
  { MP_ROM_QSTR(MP_QSTR_Y12), MP_ROM_PTR(&pin_B1_obj) },
  { MP_ROM_QSTR(MP_QSTR_SW), MP_ROM_PTR(&pin_B3_obj) },
  { MP_ROM_QSTR(MP_QSTR_LED_RED), MP_ROM_PTR(&pin_A13_obj) },
  { MP_ROM_QSTR(MP_QSTR_LED_GREEN), MP_ROM_PTR(&pin_A14_obj) },
  { MP_ROM_QSTR(MP_QSTR_LED_YELLOW), MP_ROM_PTR(&pin_A15_obj) },
  { MP_ROM_QSTR(MP_QSTR_LED_BLUE), MP_ROM_PTR(&pin_B4_obj) },
  { MP_ROM_QSTR(MP_QSTR_MMA_INT), MP_ROM_PTR(&pin_B2_obj) },
  { MP_ROM_QSTR(MP_QSTR_MMA_AVDD), MP_ROM_PTR(&pin_B5_obj) },
  { MP_ROM_QSTR(MP_QSTR_SD_D0), MP_ROM_PTR(&pin_C8_obj) },
  { MP_ROM_QSTR(MP_QSTR_SD_D1), MP_ROM_PTR(&pin_C9_obj) },
  { MP_ROM_QSTR(MP_QSTR_SD_D2), MP_ROM_PTR(&pin_C10_obj) },
  { MP_ROM_QSTR(MP_QSTR_SD_D3), MP_ROM_PTR(&pin_C11_obj) },
  { MP_ROM_QSTR(MP_QSTR_SD_CMD), MP_ROM_PTR(&pin_D2_obj) },
  { MP_ROM_QSTR(MP_QSTR_SD_CK), MP_ROM_PTR(&pin_C12_obj) },
  { MP_ROM_QSTR(MP_QSTR_SD), MP_ROM_PTR(&pin_A8_obj) },
  { MP_ROM_QSTR(MP_QSTR_SD_SW), MP_ROM_PTR(&pin_A8_obj) },
  { MP_ROM_QSTR(MP_QSTR_USB_VBUS), MP_ROM_PTR(&pin_A9_obj) },
  { MP_ROM_QSTR(MP_QSTR_USB_ID), MP_ROM_PTR(&pin_A10_obj) },
  { MP_ROM_QSTR(MP_QSTR_USB_DM), MP_ROM_PTR(&pin_A11_obj) },
  { MP_ROM_QSTR(MP_QSTR_USB_DP), MP_ROM_PTR(&pin_A12_obj) },
};
MP_DEFINE_CONST_DICT(pin_board_pins_locals_dict, pin_board_pins_locals_dict_table);

const pin_obj_t * const pin_adc1[] = {
  &pin_A0_obj, // 0
  &pin_A1_obj, // 1
  &pin_A2_obj, // 2
  &pin_A3_obj, // 3
  &pin_A4_obj, // 4
  &pin_A5_obj, // 5
  &pin_A6_obj, // 6
  &pin_A7_obj, // 7
  &pin_B0_obj, // 8
  &pin_B1_obj, // 9
  &pin_C0_obj, // 10
  &pin_C1_obj, // 11
  &pin_C2_obj, // 12
  &pin_C3_obj, // 13
  &pin_C4_obj, // 14
  &pin_C5_obj, // 15
#if defined(STM32L4)
  NULL,    // 16
#endif
};

const pin_obj_t * const pin_adc2[] = {
  &pin_A0_obj, // 0
  &pin_A1_obj, // 1
  &pin_A2_obj, // 2
  &pin_A3_obj, // 3
  &pin_A4_obj, // 4
  &pin_A5_obj, // 5
  &pin_A6_obj, // 6
  &pin_A7_obj, // 7
  &pin_B0_obj, // 8
  &pin_B1_obj, // 9
  &pin_C0_obj, // 10
  &pin_C1_obj, // 11
  &pin_C2_obj, // 12
  &pin_C3_obj, // 13
  &pin_C4_obj, // 14
  &pin_C5_obj, // 15
#if defined(STM32L4)
  NULL,    // 16
#endif
};

const pin_obj_t * const pin_adc3[] = {
  &pin_A0_obj, // 0
  &pin_A1_obj, // 1
  &pin_A2_obj, // 2
  &pin_A3_obj, // 3
  NULL,    // 4
  NULL,    // 5
  NULL,    // 6
  NULL,    // 7
  NULL,    // 8
  NULL,    // 9
  &pin_C0_obj, // 10
  &pin_C1_obj, // 11
  &pin_C2_obj, // 12
  &pin_C3_obj, // 13
  &pin_C4_obj, // 14
  &pin_C5_obj, // 15
#if defined(STM32L4)
  NULL,    // 16
#endif
};
