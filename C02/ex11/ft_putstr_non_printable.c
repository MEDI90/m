/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putstr_non_printable.c                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mboubaza <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/20 21:48:02 by mboubaza          #+#    #+#             */
/*   Updated: 2025/07/22 00:30:48 by mboubaza         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

void	ft_putchar(char c)
{
	write(1, &c, 1);
}

void	conv_hex(int dec)
{
	if (dec / 16 != 0)
		conv_hex(dec / 16);
	if (dec < 16)
		ft_putchar('0');
	ft_putchar("0123456789abcdef"[dec % 16]);
}

void	conv_hex(unsigned char dec)
{
	ft_putchar("0123456789abcdef"[dec / 16]);
	ft_putchar("0123456789abcdef"[dec % 16]);
}

void	ft_putstr_non_printable(char *str)
{
	int	i;

	i = 0;
	while (str[i] != '\0')
	{
		if (str[i] < ' ' || str[i] > '~')
		{
			write(1, "\\", 1);
			conv_hex((unsigned char)str[i]);
		}
		else
		{
			write(1, &str[i], 1);
		}
		i ++;
	}
}
