/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mboubaza <mboubaza@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/18 20:56:07 by mboubaza          #+#    #+#             */
/*   Updated: 2025/11/08 20:24:57 by mboubaza         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_memcmp(const void *s1, const void *s2, size_t n)
{
	size_t				i;
	unsigned char		*st1;
	unsigned char		*st2;

	if ((s1 == NULL && s2 == NULL))
		return (0);
	st1 = (unsigned char *)s1;
	st2 = (unsigned char *)s2;
	i = 0;
	while (i < n)
	{
		if (st1[i] != st2[i])
			return (st1[i] - st2[i]);
		i ++;
	}
	return (0);
}
