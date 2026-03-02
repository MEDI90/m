/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mboubaza <mboubaza@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/17 22:36:47 by mboubaza          #+#    #+#             */
/*   Updated: 2025/10/31 20:18:08 by mboubaza         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	ft_strlcat(char *dst, const char *src, size_t size)
{
	size_t	i;
	size_t	len;

	if (!dst)
		return (ft_strlen(src));
	if (!src)
		return (ft_strlen(dst));
	len = ft_strlen(dst);
	i = 0;
	if (size <= len)
		return (size + ft_strlen((char *)src));
	while ((size > (len + i + 1)) && src[i])
	{
		dst[len + i] = src[i];
		i++;
	}
	if (len < size)
		dst[len + i] = '\0';
	return (ft_strlen((char *)src) + len);
}
