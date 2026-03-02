/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mboubaza <mboubaza@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/19 15:36:42 by mboubaza          #+#    #+#             */
/*   Updated: 2025/11/08 20:47:23 by mboubaza         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strnstr(const char *big, const char *little, size_t len)
{
	size_t	i;
	size_t	j;

	if (little[0] == 0)
		return ((char *)big);
	i = 0;
	j = 0;
	while (big[i] && i < len)
	{
		while ((i + j) < len && big[i + j] == little[j] && big[i + j])
		{
			j ++;
			if (little[j] == 0)
				return ((char *)big + i);
		}
		j = 0;
		i ++;
	}
	return (NULL);
}
