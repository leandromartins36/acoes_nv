SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ACOESINFOMONEY](
	[DATA] [varchar](12) NOT NULL,
	[FECHAMENTO] [float] NOT NULL,
	[EMPRESA] [varchar](50) NOT NULL,
	[DT_CARGA] [date] NULL
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[ACOESINFOMONEY] ADD  CONSTRAINT [DF__ACOESINFO__DT_CA__239E4DCF]  DEFAULT (CONVERT([date],getdate())) FOR [DT_CARGA]
GO
