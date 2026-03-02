/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mboubaza <mboubaza@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/06 18:35:28 by mboubaza          #+#    #+#             */
/*   Updated: 2025/11/08 00:20:28 by mboubaza         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include "libft/libft.h"
# include <stdarg.h>
# include <unistd.h>

int	ft_printf(const char *format, ...);
int	print_char_p(char *str);
int	print_char(char c);
int	print_int(int nbr);
int	print_uint(unsigned int nbr);
int	print_hex(unsigned int nbr, char c);
int	print_addr(void *addr);

#endif