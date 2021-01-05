/****************************************************************************
 * bsp/src/chip/cxd56_adc.h
 *
 *   Copyright 2018 Sony Semiconductor Solutions Corporation
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 *
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in
 *    the documentation and/or other materials provided with the
 *    distribution.
 * 3. Neither the name of Sony Semiconductor Solutions Corporation nor
 *    the names of its contributors may be used to endorse or promote
 *    products derived from this software without specific prior written
 *    permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
 * FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
 * INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 * BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS
 * OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED
 * AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
 * ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 *
 ****************************************************************************/

#ifndef __ARCH_ARM_SRC_CXD56XX_CHIP_CXD56_ADC_H
#define __ARCH_ARM_SRC_CXD56XX_CHIP_CXD56_ADC_H

#define SCUADCIF_LPADC_A0	(CXD56_SCU_ADCIF_BASE + 0x200)
#define SCUADCIF_LPADC_A1	(CXD56_SCU_ADCIF_BASE + 0x204)
#define SCUADCIF_LPADC_D0	(CXD56_SCU_ADCIF_BASE + 0x210)
#define SCUADCIF_LPADC_D1	(CXD56_SCU_ADCIF_BASE + 0x214)
#define SCUADCIF_LPADC_D4	(CXD56_SCU_ADCIF_BASE + 0x21c)
#define SCUADCIF_LPADC_D5	(CXD56_SCU_ADCIF_BASE + 0x220)
#define SCUADCIF_LPADC_D6	(CXD56_SCU_ADCIF_BASE + 0x224)
#define SCUADCIF_LPADC_D2	(CXD56_SCU_ADCIF_BASE + 0x218)
#define SCUADCIF_HPADC_AC0	(CXD56_SCU_ADCIF_BASE + 0x240)
#define SCUADCIF_HPADC_AC1	(CXD56_SCU_ADCIF_BASE + 0x244)
#define SCUADCIF_HPADC_DC	(CXD56_SCU_ADCIF_BASE + 0x250)
#define SCUADCIF_HPADC0_A0	(CXD56_SCU_ADCIF_BASE + 0x280)
#define SCUADCIF_HPADC0_A1	(CXD56_SCU_ADCIF_BASE + 0x284)
#define SCUADCIF_HPADC0_A2	(CXD56_SCU_ADCIF_BASE + 0x288)
#define SCUADCIF_HPADC0_A3	(CXD56_SCU_ADCIF_BASE + 0x28c)
#define SCUADCIF_HPADC0_D0	(CXD56_SCU_ADCIF_BASE + 0x290)
#define SCUADCIF_HPADC0_D1	(CXD56_SCU_ADCIF_BASE + 0x294)
#define SCUADCIF_HPADC0_D2	(CXD56_SCU_ADCIF_BASE + 0x298)
#define SCUADCIF_HPADC1_A0	(CXD56_SCU_ADCIF_BASE + 0x2c0)
#define SCUADCIF_HPADC1_A1	(CXD56_SCU_ADCIF_BASE + 0x2c4)
#define SCUADCIF_HPADC1_A2	(CXD56_SCU_ADCIF_BASE + 0x2c8)
#define SCUADCIF_HPADC1_A3	(CXD56_SCU_ADCIF_BASE + 0x2cc)
#define SCUADCIF_HPADC1_D0	(CXD56_SCU_ADCIF_BASE + 0x2d0)
#define SCUADCIF_HPADC1_D1	(CXD56_SCU_ADCIF_BASE + 0x2d4)
#define SCUADCIF_HPADC1_D2	(CXD56_SCU_ADCIF_BASE + 0x2d8)
#define SCUADCIF_LPADC_AT0	(CXD56_SCU_ADCIF_BASE + 0x300)
#define SCUADCIF_LPADC_AT1	(CXD56_SCU_ADCIF_BASE + 0x304)
#define SCUADCIF_HPADC_ACT0	(CXD56_SCU_ADCIF_BASE + 0x340)
#define SCUADCIF_HPADC_ACT1	(CXD56_SCU_ADCIF_BASE + 0x344)
#define SCUADCIF_HPADC0_AT0	(CXD56_SCU_ADCIF_BASE + 0x380)
#define SCUADCIF_HPADC0_AT1	(CXD56_SCU_ADCIF_BASE + 0x384)
#define SCUADCIF_HPADC1_AT0	(CXD56_SCU_ADCIF_BASE + 0x3c0)
#define SCUADCIF_HPADC1_AT1	(CXD56_SCU_ADCIF_BASE + 0x3c4)
#define SCUADCIF_ADCIF_DCT	(CXD56_SCU_ADCIF_BASE + 0x3d0)
#define SCUADCIF_SCU_ADCIF_CKPOWER	(CXD56_SCU_ADCIF_BASE + 0x3d4)

#if 0
#define LPADC_A0_LV_ADC_EN_MASK	0x00000001
#define LPADC_A0_LV_ADC_EN_OFFSET	0
#define LPADC_A0_LV_ADC_EN_BFMASK	0x00000001
#define LPADC_A1_LV_CH_SEL_MODE_MASK	0x00000007
#define LPADC_A1_LV_CH_SEL_MODE_OFFSET	0
#define LPADC_A1_LV_CH_SEL_MODE_BFMASK	0x00000007
#define LPADC_A1_LV_CH_SEL_INV_MASK	0x00000003
#define LPADC_A1_LV_CH_SEL_INV_OFFSET	8
#define LPADC_A1_LV_CH_SEL_INV_BFMASK	0x00000300
#define LPADC_D0_SW_RESET_MASK	0x00000001
#define LPADC_D0_SW_RESET_OFFSET	0
#define LPADC_D0_SW_RESET_BFMASK	0x00000001
#define LPADC_D1_FIFO_WATERMARK_MASK	0x0000000f
#define LPADC_D1_FIFO_WATERMARK_OFFSET	0
#define LPADC_D1_FIFO_WATERMARK_BFMASK	0x0000000f
#define LPADC_D1_DMA_HS_EN_MASK	0x00000001
#define LPADC_D1_DMA_HS_EN_OFFSET	5
#define LPADC_D1_DMA_HS_EN_BFMASK	0x00000020
#define LPADC_D1_SAMP_RATIO_MASK	0x0000000f
#define LPADC_D1_SAMP_RATIO_OFFSET	8
#define LPADC_D1_SAMP_RATIO_BFMASK	0x00000f00
#define LPADC_D1_SAMP_RATIO2_MASK	0x000001ff
#define LPADC_D1_SAMP_RATIO2_OFFSET	12
#define LPADC_D1_SAMP_RATIO2_BFMASK	0x001ff000
#define LPADC_D4_FIFO_WATERMARK_MASK	0x0000000f
#define LPADC_D4_FIFO_WATERMARK_OFFSET	0
#define LPADC_D4_FIFO_WATERMARK_BFMASK	0x0000000f
#define LPADC_D4_DMA_HS_EN_MASK	0x00000001
#define LPADC_D4_DMA_HS_EN_OFFSET	5
#define LPADC_D4_DMA_HS_EN_BFMASK	0x00000020
#define LPADC_D4_SAMP_RATIO_MASK	0x0000000f
#define LPADC_D4_SAMP_RATIO_OFFSET	8
#define LPADC_D4_SAMP_RATIO_BFMASK	0x00000f00
#define LPADC_D4_SAMP_RATIO2_MASK	0x000001ff
#define LPADC_D4_SAMP_RATIO2_OFFSET	12
#define LPADC_D4_SAMP_RATIO2_BFMASK	0x001ff000
#define LPADC_D5_FIFO_WATERMARK_MASK	0x0000000f
#define LPADC_D5_FIFO_WATERMARK_OFFSET	0
#define LPADC_D5_FIFO_WATERMARK_BFMASK	0x0000000f
#define LPADC_D5_DMA_HS_EN_MASK	0x00000001
#define LPADC_D5_DMA_HS_EN_OFFSET	5
#define LPADC_D5_DMA_HS_EN_BFMASK	0x00000020
#define LPADC_D5_SAMP_RATIO_MASK	0x0000000f
#define LPADC_D5_SAMP_RATIO_OFFSET	8
#define LPADC_D5_SAMP_RATIO_BFMASK	0x00000f00
#define LPADC_D5_SAMP_RATIO2_MASK	0x000001ff
#define LPADC_D5_SAMP_RATIO2_OFFSET	12
#define LPADC_D5_SAMP_RATIO2_BFMASK	0x001ff000
#define LPADC_D6_FIFO_WATERMARK_MASK	0x0000000f
#define LPADC_D6_FIFO_WATERMARK_OFFSET	0
#define LPADC_D6_FIFO_WATERMARK_BFMASK	0x0000000f
#define LPADC_D6_DMA_HS_EN_MASK	0x00000001
#define LPADC_D6_DMA_HS_EN_OFFSET	5
#define LPADC_D6_DMA_HS_EN_BFMASK	0x00000020
#define LPADC_D6_SAMP_RATIO_MASK	0x0000000f
#define LPADC_D6_SAMP_RATIO_OFFSET	8
#define LPADC_D6_SAMP_RATIO_BFMASK	0x00000f00
#define LPADC_D6_SAMP_RATIO2_MASK	0x000001ff
#define LPADC_D6_SAMP_RATIO2_OFFSET	12
#define LPADC_D6_SAMP_RATIO2_BFMASK	0x001ff000
#define LPADC_D2_FIFO_EN_MASK	0x0000000f
#define LPADC_D2_FIFO_EN_OFFSET	0
#define LPADC_D2_FIFO_EN_BFMASK	0x0000000f
#define HPADC_AC0_LV_CLK_OSC_SEL_MASK	0x00000001
#define HPADC_AC0_LV_CLK_OSC_SEL_OFFSET	0
#define HPADC_AC0_LV_CLK_OSC_SEL_BFMASK	0x00000001
#define HPADC_AC0_LV_CLK_XOSC_DIV_MASK	0x00000003
#define HPADC_AC0_LV_CLK_XOSC_DIV_OFFSET	4
#define HPADC_AC0_LV_CLK_XOSC_DIV_BFMASK	0x00000030
#define HPADC_AC1_LV_BGR_EN_MASK	0x00000001
#define HPADC_AC1_LV_BGR_EN_OFFSET	0
#define HPADC_AC1_LV_BGR_EN_BFMASK	0x00000001
#define HPADC_DC_VECTOR_SEL_MASK	0x00000001
#define HPADC_DC_VECTOR_SEL_OFFSET	0
#define HPADC_DC_VECTOR_SEL_BFMASK	0x00000001
#define HPADC0_A0_LV_CLK_U32_SEL0_MASK	0x00000001
#define HPADC0_A0_LV_CLK_U32_SEL0_OFFSET	0
#define HPADC0_A0_LV_CLK_U32_SEL0_BFMASK	0x00000001
#define HPADC0_A1_LV_ADC0_EN_MASK	0x00000001
#define HPADC0_A1_LV_ADC0_EN_OFFSET	0
#define HPADC0_A1_LV_ADC0_EN_BFMASK	0x00000001
#define HPADC0_A1_LV_LPF0_EN_MASK	0x00000001
#define HPADC0_A1_LV_LPF0_EN_OFFSET	1
#define HPADC0_A1_LV_LPF0_EN_BFMASK	0x00000002
#define HPADC0_A1_LV_ADC0_REF_EN_MASK	0x00000001
#define HPADC0_A1_LV_ADC0_REF_EN_OFFSET	2
#define HPADC0_A1_LV_ADC0_REF_EN_BFMASK	0x00000004
#define HPADC0_A2_LV_CLKOUT0_EN_MASK	0x00000001
#define HPADC0_A2_LV_CLKOUT0_EN_OFFSET	0
#define HPADC0_A2_LV_CLKOUT0_EN_BFMASK	0x00000001
#define HPADC0_A3_LV_ADC0_PREAMPLP_EN_MASK	0x00000001
#define HPADC0_A3_LV_ADC0_PREAMPLP_EN_OFFSET	0
#define HPADC0_A3_LV_ADC0_PREAMPLP_EN_BFMASK	0x00000001
#define HPADC0_A3_LV_ADC0_REFLP_EN_MASK	0x00000001
#define HPADC0_A3_LV_ADC0_REFLP_EN_OFFSET	1
#define HPADC0_A3_LV_ADC0_REFLP_EN_BFMASK	0x00000002
#define HPADC0_A3_LV_ADC0_REFCTRL_MASK	0x0000000f
#define HPADC0_A3_LV_ADC0_REFCTRL_OFFSET	4
#define HPADC0_A3_LV_ADC0_REFCTRL_BFMASK	0x000000f0
#define HPADC0_A3_LV_LPF0_XSTARTUP_MASK	0x00000001
#define HPADC0_A3_LV_LPF0_XSTARTUP_OFFSET	8
#define HPADC0_A3_LV_LPF0_XSTARTUP_BFMASK	0x00000100
#define HPADC0_A3_LV_LPF0_FC_MASK	0x00000003
#define HPADC0_A3_LV_LPF0_FC_OFFSET	10
#define HPADC0_A3_LV_LPF0_FC_BFMASK	0x00000c00
#define HPADC0_A3_LV_LPF0_GAIN1ST_MASK	0x0000000f
#define HPADC0_A3_LV_LPF0_GAIN1ST_OFFSET	12
#define HPADC0_A3_LV_LPF0_GAIN1ST_BFMASK	0x0000f000
#define HPADC0_A3_LV_LPF0_GAIN2ND_MASK	0x0000000f
#define HPADC0_A3_LV_LPF0_GAIN2ND_OFFSET	16
#define HPADC0_A3_LV_LPF0_GAIN2ND_BFMASK	0x000f0000
#define HPADC0_A3_LV_LPF0_MODE_MASK	0x00000007
#define HPADC0_A3_LV_LPF0_MODE_OFFSET	20
#define HPADC0_A3_LV_LPF0_MODE_BFMASK	0x00700000
#define HPADC0_A3_LV_LPF0_ATT_SEL_MASK	0x00000003
#define HPADC0_A3_LV_LPF0_ATT_SEL_OFFSET	24
#define HPADC0_A3_LV_LPF0_ATT_SEL_BFMASK	0x03000000
#define HPADC0_D0_SW_RESET_MASK	0x00000001
#define HPADC0_D0_SW_RESET_OFFSET	0
#define HPADC0_D0_SW_RESET_BFMASK	0x00000001
#define HPADC0_D1_FIFO_WATERMARK_MASK	0x0000001f
#define HPADC0_D1_FIFO_WATERMARK_OFFSET	0
#define HPADC0_D1_FIFO_WATERMARK_BFMASK	0x0000001f
#define HPADC0_D1_DMA_HS_EN_MASK	0x00000001
#define HPADC0_D1_DMA_HS_EN_OFFSET	5
#define HPADC0_D1_DMA_HS_EN_BFMASK	0x00000020
#define HPADC0_D1_DECI_RATIO_MASK	0x00000007
#define HPADC0_D1_DECI_RATIO_OFFSET	8
#define HPADC0_D1_DECI_RATIO_BFMASK	0x00000700
#define HPADC0_D1_DECI_RATIO2_MASK	0x000001ff
#define HPADC0_D1_DECI_RATIO2_OFFSET	12
#define HPADC0_D1_DECI_RATIO2_BFMASK	0x001ff000
#define HPADC0_D2_DECIFIFO_EN_MASK	0x00000001
#define HPADC0_D2_DECIFIFO_EN_OFFSET	0
#define HPADC0_D2_DECIFIFO_EN_BFMASK	0x00000001
#define HPADC1_A0_LV_CLK_U32_SEL1_MASK	0x00000001
#define HPADC1_A0_LV_CLK_U32_SEL1_OFFSET	0
#define HPADC1_A0_LV_CLK_U32_SEL1_BFMASK	0x00000001
#define HPADC1_A1_LV_ADC1_EN_MASK	0x00000001
#define HPADC1_A1_LV_ADC1_EN_OFFSET	0
#define HPADC1_A1_LV_ADC1_EN_BFMASK	0x00000001
#define HPADC1_A1_LV_LPF1_EN_MASK	0x00000001
#define HPADC1_A1_LV_LPF1_EN_OFFSET	1
#define HPADC1_A1_LV_LPF1_EN_BFMASK	0x00000002
#define HPADC1_A1_LV_ADC1_REF_EN_MASK	0x00000001
#define HPADC1_A1_LV_ADC1_REF_EN_OFFSET	2
#define HPADC1_A1_LV_ADC1_REF_EN_BFMASK	0x00000004
#define HPADC1_A2_LV_CLKOUT1_EN_MASK	0x00000001
#define HPADC1_A2_LV_CLKOUT1_EN_OFFSET	0
#define HPADC1_A2_LV_CLKOUT1_EN_BFMASK	0x00000001
#define HPADC1_A3_LV_ADC1_PREAMPLP_EN_MASK	0x00000001
#define HPADC1_A3_LV_ADC1_PREAMPLP_EN_OFFSET	0
#define HPADC1_A3_LV_ADC1_PREAMPLP_EN_BFMASK	0x00000001
#define HPADC1_A3_LV_ADC1_REFLP_EN_MASK	0x00000001
#define HPADC1_A3_LV_ADC1_REFLP_EN_OFFSET	1
#define HPADC1_A3_LV_ADC1_REFLP_EN_BFMASK	0x00000002
#define HPADC1_A3_LV_ADC1_REFCTRL_MASK	0x0000000f
#define HPADC1_A3_LV_ADC1_REFCTRL_OFFSET	4
#define HPADC1_A3_LV_ADC1_REFCTRL_BFMASK	0x000000f0
#define HPADC1_A3_LV_LPF1_XSTARTUP_MASK	0x00000001
#define HPADC1_A3_LV_LPF1_XSTARTUP_OFFSET	8
#define HPADC1_A3_LV_LPF1_XSTARTUP_BFMASK	0x00000100
#define HPADC1_A3_LV_LPF1_FC_MASK	0x00000003
#define HPADC1_A3_LV_LPF1_FC_OFFSET	10
#define HPADC1_A3_LV_LPF1_FC_BFMASK	0x00000c00
#define HPADC1_A3_LV_LPF1_GAIN1ST_MASK	0x0000000f
#define HPADC1_A3_LV_LPF1_GAIN1ST_OFFSET	12
#define HPADC1_A3_LV_LPF1_GAIN1ST_BFMASK	0x0000f000
#define HPADC1_A3_LV_LPF1_GAIN2ND_MASK	0x0000000f
#define HPADC1_A3_LV_LPF1_GAIN2ND_OFFSET	16
#define HPADC1_A3_LV_LPF1_GAIN2ND_BFMASK	0x000f0000
#define HPADC1_A3_LV_LPF1_MODE_MASK	0x00000007
#define HPADC1_A3_LV_LPF1_MODE_OFFSET	20
#define HPADC1_A3_LV_LPF1_MODE_BFMASK	0x00700000
#define HPADC1_A3_LV_LPF1_ATT_SEL_MASK	0x00000003
#define HPADC1_A3_LV_LPF1_ATT_SEL_OFFSET	24
#define HPADC1_A3_LV_LPF1_ATT_SEL_BFMASK	0x03000000
#define HPADC1_D0_SW_RESET_MASK	0x00000001
#define HPADC1_D0_SW_RESET_OFFSET	0
#define HPADC1_D0_SW_RESET_BFMASK	0x00000001
#define HPADC1_D1_FIFO_WATERMARK_MASK	0x0000001f
#define HPADC1_D1_FIFO_WATERMARK_OFFSET	0
#define HPADC1_D1_FIFO_WATERMARK_BFMASK	0x0000001f
#define HPADC1_D1_DMA_HS_EN_MASK	0x00000001
#define HPADC1_D1_DMA_HS_EN_OFFSET	5
#define HPADC1_D1_DMA_HS_EN_BFMASK	0x00000020
#define HPADC1_D1_DECI_RATIO_MASK	0x00000007
#define HPADC1_D1_DECI_RATIO_OFFSET	8
#define HPADC1_D1_DECI_RATIO_BFMASK	0x00000700
#define HPADC1_D1_DECI_RATIO2_MASK	0x000001ff
#define HPADC1_D1_DECI_RATIO2_OFFSET	12
#define HPADC1_D1_DECI_RATIO2_BFMASK	0x001ff000
#define HPADC1_D2_DECIFIFO_EN_MASK	0x00000001
#define HPADC1_D2_DECIFIFO_EN_OFFSET	0
#define HPADC1_D2_DECIFIFO_EN_BFMASK	0x00000001
#define LPADC_AT0_LV_SELSTAGE_MASK	0x00000001
#define LPADC_AT0_LV_SELSTAGE_OFFSET	0
#define LPADC_AT0_LV_SELSTAGE_BFMASK	0x00000001
#define LPADC_AT0_LV_DELAYADJUST_MASK	0x0000000f
#define LPADC_AT0_LV_DELAYADJUST_OFFSET	4
#define LPADC_AT0_LV_DELAYADJUST_BFMASK	0x000000f0
#define LPADC_AT0_LV_ENSHIFTP_MASK	0x00000007
#define LPADC_AT0_LV_ENSHIFTP_OFFSET	12
#define LPADC_AT0_LV_ENSHIFTP_BFMASK	0x00007000
#define LPADC_AT0_LV_ENSHIFTM_MASK	0x00000007
#define LPADC_AT0_LV_ENSHIFTM_OFFSET	16
#define LPADC_AT0_LV_ENSHIFTM_BFMASK	0x00070000
#define LPADC_AT1_LV_RSV_MASK	0x000000ff
#define LPADC_AT1_LV_RSV_OFFSET	0
#define LPADC_AT1_LV_RSV_BFMASK	0x000000ff
#define LPADC_AT1_LV_ATB_EN_MASK	0x00000001
#define LPADC_AT1_LV_ATB_EN_OFFSET	9
#define LPADC_AT1_LV_ATB_EN_BFMASK	0x00000200
#define LPADC_AT1_LV_ATB_SEL_MASK	0x0000000f
#define LPADC_AT1_LV_ATB_SEL_OFFSET	12
#define LPADC_AT1_LV_ATB_SEL_BFMASK	0x0000f000
#define HPADC_ACT0_LV_LPF_ATB_SEL_MASK	0x0000000f
#define HPADC_ACT0_LV_LPF_ATB_SEL_OFFSET	0
#define HPADC_ACT0_LV_LPF_ATB_SEL_BFMASK	0x0000000f
#define HPADC_ACT0_LV_LPF_RSV_MASK	0x0000000f
#define HPADC_ACT0_LV_LPF_RSV_OFFSET	4
#define HPADC_ACT0_LV_LPF_RSV_BFMASK	0x000000f0
#define HPADC_ACT1_LV_BGR_TRIM_MASK	0x00000007
#define HPADC_ACT1_LV_BGR_TRIM_OFFSET	0
#define HPADC_ACT1_LV_BGR_TRIM_BFMASK	0x00000007
#define HPADC_ACT1_LV_BGR_TST_EN_MASK	0x00000001
#define HPADC_ACT1_LV_BGR_TST_EN_OFFSET	4
#define HPADC_ACT1_LV_BGR_TST_EN_BFMASK	0x00000010
#define HPADC0_AT0_LV_ADC0_SELSTAGE_MASK	0x00000001
#define HPADC0_AT0_LV_ADC0_SELSTAGE_OFFSET	0
#define HPADC0_AT0_LV_ADC0_SELSTAGE_BFMASK	0x00000001
#define HPADC0_AT0_LV_ADC0_DELAYADJUST_MASK	0x0000000f
#define HPADC0_AT0_LV_ADC0_DELAYADJUST_OFFSET	4
#define HPADC0_AT0_LV_ADC0_DELAYADJUST_BFMASK	0x000000f0
#define HPADC0_AT0_LV_ADC0_ENSHIFTP_MASK	0x00000007
#define HPADC0_AT0_LV_ADC0_ENSHIFTP_OFFSET	8
#define HPADC0_AT0_LV_ADC0_ENSHIFTP_BFMASK	0x00000700
#define HPADC0_AT0_LV_ADC0_ENSHIFTM_MASK	0x00000007
#define HPADC0_AT0_LV_ADC0_ENSHIFTM_OFFSET	12
#define HPADC0_AT0_LV_ADC0_ENSHIFTM_BFMASK	0x00007000
#define HPADC0_AT1_LV_ADC0_RSV_MASK	0x0000000f
#define HPADC0_AT1_LV_ADC0_RSV_OFFSET	0
#define HPADC0_AT1_LV_ADC0_RSV_BFMASK	0x0000000f
#define HPADC0_AT1_LV_ADC0_REFEXT_EN_MASK	0x00000001
#define HPADC0_AT1_LV_ADC0_REFEXT_EN_OFFSET	4
#define HPADC0_AT1_LV_ADC0_REFEXT_EN_BFMASK	0x00000010
#define HPADC0_AT1_LV_ADC0_ATB_EN_MASK	0x00000001
#define HPADC0_AT1_LV_ADC0_ATB_EN_OFFSET	5
#define HPADC0_AT1_LV_ADC0_ATB_EN_BFMASK	0x00000020
#define HPADC0_AT1_LV_ADC0_ATB_SEL_MASK	0x0000000f
#define HPADC0_AT1_LV_ADC0_ATB_SEL_OFFSET	8
#define HPADC0_AT1_LV_ADC0_ATB_SEL_BFMASK	0x00000f00
#define HPADC1_AT0_LV_ADC1_SELSTAGE_MASK	0x00000001
#define HPADC1_AT0_LV_ADC1_SELSTAGE_OFFSET	0
#define HPADC1_AT0_LV_ADC1_SELSTAGE_BFMASK	0x00000001
#define HPADC1_AT0_LV_ADC1_DELAYADJUST_MASK	0x0000000f
#define HPADC1_AT0_LV_ADC1_DELAYADJUST_OFFSET	4
#define HPADC1_AT0_LV_ADC1_DELAYADJUST_BFMASK	0x000000f0
#define HPADC1_AT0_LV_ADC1_ENSHIFTP_MASK	0x00000007
#define HPADC1_AT0_LV_ADC1_ENSHIFTP_OFFSET	8
#define HPADC1_AT0_LV_ADC1_ENSHIFTP_BFMASK	0x00000700
#define HPADC1_AT0_LV_ADC1_ENSHIFTM_MASK	0x00000007
#define HPADC1_AT0_LV_ADC1_ENSHIFTM_OFFSET	12
#define HPADC1_AT0_LV_ADC1_ENSHIFTM_BFMASK	0x00007000
#define HPADC1_AT1_LV_ADC1_RSV_MASK	0x0000000f
#define HPADC1_AT1_LV_ADC1_RSV_OFFSET	0
#define HPADC1_AT1_LV_ADC1_RSV_BFMASK	0x0000000f
#define HPADC1_AT1_LV_ADC1_REFEXT_EN_MASK	0x00000001
#define HPADC1_AT1_LV_ADC1_REFEXT_EN_OFFSET	4
#define HPADC1_AT1_LV_ADC1_REFEXT_EN_BFMASK	0x00000010
#define HPADC1_AT1_LV_ADC1_ATB_EN_MASK	0x00000001
#define HPADC1_AT1_LV_ADC1_ATB_EN_OFFSET	5
#define HPADC1_AT1_LV_ADC1_ATB_EN_BFMASK	0x00000020
#define HPADC1_AT1_LV_ADC1_ATB_SEL_MASK	0x0000000f
#define HPADC1_AT1_LV_ADC1_ATB_SEL_OFFSET	8
#define HPADC1_AT1_LV_ADC1_ATB_SEL_BFMASK	0x00000f00
#define ADCIF_DCT_REV_CODE_MASK	0xffffffff
#define ADCIF_DCT_REV_CODE_OFFSET	0
#define ADCIF_DCT_REV_CODE_BFMASK	0xffffffff
#define SCU_ADCIF_CKPOWER_CK_POWEREN_MASK	0x00000001
#define SCU_ADCIF_CKPOWER_CK_POWEREN_OFFSET	0
#define SCU_ADCIF_CKPOWER_CK_POWEREN_BFMASK	0x00000001
#endif

#endif /* __ARCH_ARM_SRC_CXD56XX_CHIP_CXD56_ADC_H */