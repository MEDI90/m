/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mboubaza <mboubaza@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/19 23:56:19 by mboubaza          #+#    #+#             */
/*   Updated: 2025/11/04 15:01:29 by mboubaza         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_calloc(size_t nelem, size_t elsize)
{
	void	*cal;

	if (elsize != 0 && nelem > __SIZE_MAX__ / elsize)
		return (NULL);
	if (nelem == 0 || elsize == 0)
	{
		cal = malloc(1);
		if (!cal)
			return (NULL);
		return (cal);
	}
	cal = malloc(nelem * elsize);
	if (!cal)
		return (NULL);
	ft_bzero(cal, nelem * elsize);
	return (cal);
}
