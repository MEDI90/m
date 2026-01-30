NAME		= push_swap
CC		= cc
CFLAGS		= -Wall -Wextra -Werror

# Directories
MOVES_DIR	= ./moves


# Source Files
SRCS		= main.c \
			  init.c \
			  init_utils.c \
			  init_target.c \
			  turk.c \
			  list_utils.c \
			  ./libft/ft_split.c\
			  safe_atoi.c \
			  $(MOVES_DIR)/push.c \
			  $(MOVES_DIR)/swap.c \
			  $(MOVES_DIR)/rotate.c \
			  $(MOVES_DIR)/rev_rotate.c

OBJS		= $(SRCS:.c=.o)

# Rules
all: $(NAME)

$(NAME): $(LIBFT) $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -o $(NAME)


%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJS)

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re
