/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mboubaza <mboubaza@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/28 13:25:59 by mboubaza          #+#    #+#             */
/*   Updated: 2025/11/02 18:34:25 by mboubaza         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	word_counter(char *str, char c)
{
	int	f;
	int	i;
	int	w;

	i = 0;
	w = 1;
	f = 0;
	if (!str)
		return (-1);
	if (str[0] == c)
	{
		f = 1;
		w = 0;
	}
	while (str[++i])
	{
		if (str[i] != c && f == 1)
		{
			f = 0;
			w++;
		}
		else if (str[i] == c)
			f = 1;
	}
	return (w);
}

int	char_count(char *str, int index, char c)
{
	while (str[index] && str[index] != c)
		index++;
	return (index);
}

static char	**ft_free(char **str, int index)
{
	int	i;

	i = 0;
	while (i < index)
		free(str[i++]);
	free(str);
	return (NULL);
}

char	**ft_split(char const *s, char c)
{
	char	**str;
	int		i;
	int		j;
	int		k;
	int		index;

	i = 0;
	j = 0;
	str = malloc(sizeof(char *) * (word_counter((char *)s, c) + 1));
	if (!s || !str)
		return (ft_free(str, 0));
	while (j < word_counter((char *)s, c) && s[i])
	{
		while (s[i] == c)
			i++;
		index = char_count((char *)s, i, c);
		str[j] = malloc(sizeof(char) * (index - i + 1));
		if (!str[j])
			return (ft_free(str, i));
		k = 0;
		while (i < index)
			str[j][k++] = (char)s[i++];
		str[j++][k] = '\0';
	}
	return (str[j] = NULL, str);
}
