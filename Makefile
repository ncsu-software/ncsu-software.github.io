MAKEFLAGS += --silent
SHELL=/bin/bash
Top=$(shell git rev-parse --show-toplevel)

# One-file trick: the nvim and bash configs live at the bottom of this
# Makefile as "#vi " and "#sh " comment lines. Rules grep them out into $(Rc).
Me := $(abspath $(lastword $(MAKEFILE_LIST)))
Rc := $(HOME)/.cache/mk/$(notdir $(Top))
Nvim = nvim --clean -u $(Rc)/init.lua

ifeq ($(origin vi),command line)  # "make vi=file" needs no target
.DEFAULT_GOAL := vi
endif

help: ## print help
	gawk 'BEGIN {FS = ":.*?## "; print "\nmake: [OPTIONS]\n"}\
	          /^[a-z].*##/     {printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

pull: ## download
	git pull

push: ## save
	echo -en "\033[33mWhy this push? \033[0m"; read x; git commit -am "$$x"; git push; git status

view: ## build+serve locally, open browser on the top page when ready
	( until curl -so /dev/null http://127.0.0.1:4000/; do sleep 1; done; \
	  open http://127.0.0.1:4000/ ) &
	PATH="$$(ls -d /opt/homebrew/opt/ruby@3.3/bin /opt/homebrew/opt/ruby@3.4/bin 2>/dev/null | head -1):$$PATH" \
	  bundle exec jekyll serve

Ruby = PATH="$$(ls -d /opt/homebrew/opt/ruby@3.3/bin /opt/homebrew/opt/ruby@3.4/bin 2>/dev/null | head -1):$$PATH"

a11y: ## build, then scan every page for WCAG 2.1 AA problems (see accessibility.md)
	rm -rf _site        # a stale _site keeps deleted pages in the nav
	$(Ruby) bundle exec jekyll build
	[ -d tools/a11y/node_modules ] || (cd tools/a11y && npm install)
	python3 -m http.server 4100 --bind 127.0.0.1 -d _site >/dev/null 2>&1 & \
	  srv=$$!; sleep 2; \
	  (cd tools/a11y && node scan.js); rc=$$?; \
	  kill $$srv; exit $$rc

all: ## stamp README's header (after front matter, before first h1) on every *.md
	for f in *.md; do \
	  [ "$$f" = "README.md" ] && continue; \
	  [ "$$f" = "accessibility.md" ] && continue; \
	  { gawk 'NR==1 && /^---$$/{fm=1} fm{print} fm && NR>1 && /^---$$/{exit}' $$f; \
	    gawk 'NR==1 && /^---$$/{fm=1; next} fm && /^---$$/{fm=0; next} fm{next} /^# /{exit} {print}' README.md; \
	    gawk '/^# /{p=1}p' $$f; } > $$f.tmp \
	  && mv $$f.tmp $$f; \
	done

$(Rc)/init.lua: $(Me)
	mkdir -p $(Rc); sed -n -E 's/^#vi ?//p' $(Me) > $@

$(Rc)/bashrc: $(Me)
	mkdir -p $(Rc); sed -n -E 's/^#sh ?//p' $(Me) > $@

vi: $(Rc)/init.lua ## edit: make vi=file  (nvim --clean + config from this Makefile)
	$(Nvim) $(vi)

sh: $(Rc)/init.lua $(Rc)/bashrc ## tuned bash (config from this Makefile)
	env -u MAKEFLAGS -u MFLAGS -u MAKELEVEL here=$(Top) rc=$(Rc) \
	  bash --rcfile $(Rc)/bashrc -i || true

.PHONY: help pull push view a11y all vi sh

# ---------------------------------------------- bash config (make sh)
#sh # tuned interactive bash; enter via `make sh`, which sets
#sh #   here = repo root   rc = dir holding the configs grepped out of the Makefile
#sh here="${here:-$PWD}"
#sh me=$(basename "$here" | tr a-z A-Z)
#sh bold=$(tput bold); col1=$(tput setaf 6); col2=$(tput setaf 3); col0=$(tput sgr0)
#sh meme="${bold}${col1}$me${col0}"
#sh
#sh hi() {
#sh   clear; echo -n "$bold$col1"; figlet -W -f slant "$me" 2>/dev/null || echo "$me"
#sh   echo -n "$col2"; aliases; echo -n "$col0"; }
#sh
#sh aliases() {
#sh   echo "Short cuts:"
#sh   alias | sed 's/alias /  /'
#sh   echo ""; }
#sh
#sh there() { cd "$1"; basename "$(pwd)"; }
#sh
#sh alias ..='cd ..'
#sh alias ...='cd ../../../'
#sh alias h="history"
#sh alias ls="ls -G"
#sh alias py="python3 -B "
#sh alias vi="nvim --clean -u $rc/init.lua"
#sh alias mace="make -C .."
#sh alias ,="make"
#sh # ",rule" or ",vi=file" (no space) ==> make rule / make vi=file   (bash >= 4)
#sh command_not_found_handle() {
#sh   case "$1" in ,?*) make "${1#,}" "${@:2}";; *) echo "bash: $1: command not found" >&2; return 127;; esac; }
#sh
#sh export BASH_SILENCE_DEPRECATION_WARNING=1
#sh export PATH="$here:/opt/homebrew/bin:$PATH"
#sh export EDITOR=nvim
#sh
#sh PROMPT_COMMAND='echo -ne "${meme}!$(git branch 2>/dev/null | grep '\''^*'\'' | colrm 1 2) ";PS1="$(there ..)/$(there .):\!\[\e[m\] \$ "'
#sh hi
#sh # per-repo extras, if any
#sh [ -f "$here/bashrc.local" ] && . "$here/bashrc.local"

# ---------------------------------------------- nvim config (make vi=file)
#vi -- Neovim config (nvim >= 0.12, vim.pack). launch: make vi=file
#vi -- keys: <space>f files  <space>g grep  <space>b buffers  <space>t todos
#vi --       <space>e files-float  -  sidebar  <tab>/<s-tab> buffers
#vi --       <space>? keymap help  ]h/[h hunks  <space>hs stage  <space>hr reset
#vi local o, map, au = vim.o, vim.keymap.set, vim.api.nvim_create_autocmd
#vi vim.g.mapleader = " "
#vi o.termguicolors, o.number, o.cursorline, o.signcolumn = true, true, true, "yes"
#vi o.expandtab, o.shiftwidth, o.tabstop, o.softtabstop = true, 2, 2, 2
#vi o.ignorecase, o.smartcase, o.clipboard = true, true, "unnamedplus"
#vi o.splitbelow, o.splitright, o.scrolloff, o.undofile = true, true, 6, true
#vi o.autoread, o.updatetime, o.timeoutlen = true, 250, 400
#vi
#vi -- autoread needs a poll: re-check on idle / buffer-enter / focus.
#vi au({ "FocusGained", "BufEnter", "CursorHold", "CursorHoldI" }, {
#vi   callback = function()
#vi     if vim.fn.mode() ~= "c" and vim.fn.getcmdwintype() == "" then vim.cmd("checktime") end
#vi   end })
#vi au("TextYankPost", { callback = function() vim.hl.on_yank() end })
#vi
#vi -- plugins. --clean drops site from packpath/rtp; re-add it.
#vi local site = vim.fn.stdpath("data") .. "/site"
#vi vim.opt.packpath:prepend(site)
#vi vim.opt.runtimepath:prepend(site)
#vi vim.g.loaded_netrw, vim.g.loaded_netrwPlugin = 1, 1   -- oil replaces netrw
#vi vim.pack.add({
#vi   "https://github.com/catppuccin/nvim",
#vi   "https://github.com/nvim-lua/plenary.nvim",         -- for todo-comments
#vi   "https://github.com/echasnovski/mini.nvim",
#vi   "https://github.com/nvim-treesitter/nvim-treesitter",
#vi   "https://github.com/nvim-treesitter/nvim-treesitter-context",
#vi   "https://github.com/HiPhish/rainbow-delimiters.nvim",
#vi   "https://github.com/stevearc/oil.nvim",
#vi   "https://github.com/lewis6991/gitsigns.nvim",
#vi   "https://github.com/folke/which-key.nvim",
#vi   "https://github.com/julienvincent/nvim-paredit",
#vi   "https://github.com/folke/todo-comments.nvim",
#vi })
#vi vim.cmd.colorscheme("catppuccin-mocha")
#vi
#vi -- mini: icons, fuzzy pick, statusline, tabline, pairs, surround, comment
#vi for _, m in ipairs({ "icons", "pick", "statusline", "tabline", "pairs", "surround", "comment" }) do
#vi   require("mini." .. m).setup()
#vi end
#vi map("n", "<leader>f", "<cmd>Pick files<CR>")
#vi map("n", "<leader>g", "<cmd>Pick grep_live<CR>")
#vi map("n", "<leader>b", "<cmd>Pick buffers<CR>")
#vi map("n", "<tab>", "<cmd>bnext<CR>")
#vi map("n", "<s-tab>", "<cmd>bprev<CR>")
#vi
#vi -- treesitter: parsers auto-installed (needs tree-sitter cli + cc)
#vi local langs = { "lua", "python", "commonlisp", "markdown", "bash", "make", "json" }
#vi require("nvim-treesitter").install(langs)
#vi au("FileType", { callback = function(a)
#vi   pcall(vim.treesitter.start, a.buf)
#vi   vim.bo[a.buf].indentexpr = "v:lua.require'nvim-treesitter'.indentexpr()"
#vi end })
#vi require("treesitter-context").setup({ max_lines = 3 })
#vi
#vi -- files: oil edits dirs as buffers
#vi require("oil").setup({ view_options = { show_hidden = true },
#vi   keymaps = {                                          -- in oil: - parent, q close
#vi     q = function() vim.api.nvim_win_close(0, true) end,
#vi     ["<CR>"] = function()                              -- dir: enter; file: open in other window
#vi       local oil, e = require("oil"), require("oil").get_cursor_entry()
#vi       if not e then return elseif e.type == "directory" then return oil.select() end
#vi       local path, win = oil.get_current_dir() .. e.name, nil
#vi       for _, w in ipairs(vim.api.nvim_list_wins()) do
#vi         if vim.bo[vim.api.nvim_win_get_buf(w)].filetype ~= "oil" then win = w break end end
#vi       if win then vim.api.nvim_set_current_win(win) else vim.cmd("botright vsplit") end
#vi       vim.cmd.edit(vim.fn.fnameescape(path))
#vi     end } })
#vi map("n", "-", function()                              -- toggle left sidebar
#vi   for _, w in ipairs(vim.api.nvim_list_wins()) do
#vi     if vim.bo[vim.api.nvim_win_get_buf(w)].filetype == "oil" then
#vi       return vim.api.nvim_win_close(w, true) end end
#vi   vim.cmd("topleft 30vsplit | Oil")
#vi end)
#vi map("n", "<leader>e", function() require("oil").toggle_float() end)
#vi
#vi -- git gutter
#vi require("gitsigns").setup({ on_attach = function(b)
#vi   local gs = require("gitsigns")
#vi   map("n", "]h", function() gs.nav_hunk("next") end, { buffer = b })
#vi   map("n", "[h", function() gs.nav_hunk("prev") end, { buffer = b })
#vi   map("n", "<leader>hs", gs.stage_hunk, { buffer = b })
#vi   map("n", "<leader>hr", gs.reset_hunk, { buffer = b })
#vi   map("n", "<leader>hp", gs.preview_hunk, { buffer = b })
#vi end })
#vi
#vi require("which-key").setup({ preset = "helix" })
#vi map("n", "<leader>?", function() require("which-key").show({ global = false }) end)
#vi require("todo-comments").setup()
#vi map("n", "<leader>t", "<cmd>TodoQuickFix<CR>")
#vi
#vi -- lisp: vim indenting + this repo's kit words; paredit slurp/barf/raise
#vi au("FileType", { pattern = "lisp", callback = function()
#vi   vim.opt_local.lisp = true
#vi   vim.opt_local.lispwords:append({ "fn", "let+", "defmethod", "loop" })
#vi end })
#vi require("nvim-paredit").setup()
#vi
#vi -- per-repo overrides (loaded last so they win). silent if missing.
#vi pcall(dofile, vim.fn.getcwd() .. "/init.local.lua")
