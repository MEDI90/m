/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mboubaza <mboubaza@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/06 18:11:58 by mboubaza          #+#    #+#             */
/*   Updated: 2025/12/14 15:07:39 by mboubaza         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

static int	which_to_pr(const char *format, va_list args)
{
	if (*format == 'd' || *format == 'i')
		return (print_int((int)va_arg(args, int)));
	else if (*format == 's')
		return (print_char_p((char *)va_arg(args, char *)));
	else if (*format == 'c')
		return (print_char((char)va_arg(args, int)));
	else if (*format == 'u')
		return (print_uint((unsigned int)va_arg(args, unsigned int)));
	else if (*format == 'x' || *format == 'X')
		return (print_hex(va_arg(args, unsigned int), *format));
	else if (*format == 'p')
		return (print_addr(va_arg(args, void *)));
	else if (*format == '%')
	{
		write(1, "%", 1);
		return (1);
	}
	else
	{
		write(1, "%", 1);
		write(1, format, 1);
		return (2);
	}
	return (0);
}

int	ft_printf(const char *format, ...)
{
	int		count;
	va_list	args;

	if (!format || write(1, NULL, 0) == -1)
		return (-1);
	va_start(args, format);
	count = 0;
	while (*format)
	{
		if (*format == '%' && *(format + 1) == 0)
			return (-1);
		if (*format == '%')
		{
			format++;
			count += which_to_pr(format, args);
		}
		else if (*format != '%')
		{
			write(1, format, 1);
			count++;
		}
		format++;
	}
	va_end(args);
	return (count);
}
