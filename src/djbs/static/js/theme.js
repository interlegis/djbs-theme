/*!
 * Color mode toggler for Bootstrap's docs (https://getbootstrap.com/)
 * Copyright 2011-2024 The Bootstrap Authors
 * Licensed under the Creative Commons Attribution 3.0 Unported License.
 */

(() => {
  'use strict'

  const getStoredTheme = () => localStorage.getItem('theme')
  const setStoredTheme = theme => localStorage.setItem('theme', theme)

  const getPreferredTheme = () => {
    const storedTheme = getStoredTheme()
    if (storedTheme) {
      return storedTheme
    }

    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
  }

  const setTheme = theme => {
    if (theme === 'auto') {
      document.documentElement.setAttribute('data-bs-theme', (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'))
    } else {
      document.documentElement.setAttribute('data-bs-theme', theme)
    }
  }

  setTheme(getPreferredTheme())

  const showActiveTheme = (theme, focus = false) => {
    const themeSwitcher = document.querySelector('#bd-theme')

    if (!themeSwitcher) {
      return
    }

    const themeSwitcherText = document.querySelector('#bd-theme-text');
    // const activeThemeIcon = document.querySelector('.theme-icon-active')
    const btnToActive = document.querySelector(`[data-bs-theme-value="${theme}"]`)
    const iconOfActiveBtn = btnToActive.querySelector(`[data-bs-theme-value="${theme}"] i.bi`).dataset.iconName

    document.querySelectorAll('[data-bs-theme-value]').forEach(element => {
      element.classList.remove('active')
      element.setAttribute('aria-pressed', 'false')
    })

    btnToActive.classList.add('active')
    btnToActive.setAttribute('aria-pressed', 'true')
    const themeSwitcherLabel = `${themeSwitcherText.textContent} (${btnToActive.dataset.bsThemeValue})`
    themeSwitcher.setAttribute('aria-label', themeSwitcherLabel)

    if (focus) {
      themeSwitcher.focus()
    }
  }

  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => {
    const storedTheme = getStoredTheme()
    if (storedTheme !== 'light' && storedTheme !== 'dark') {
      setTheme(getPreferredTheme())
    }
  })

  window.addEventListener('DOMContentLoaded', () => {
    showActiveTheme(getPreferredTheme())

    document.querySelectorAll('[data-bs-theme-value]')
      .forEach(toggle => {
        toggle.addEventListener('click', () => {
          const theme = toggle.getAttribute('data-bs-theme-value')
          setStoredTheme(theme)
          setTheme(theme)
          showActiveTheme(theme, true)
        })
      })
  })
  document.addEventListener("DOMContentLoaded", function() {
    const renderedWidgets = document.querySelectorAll(".related-widget-wrapper");

    function applyStyles(widget) {
        // Adiciona classes do Bootstrap aos elementos de formulário dentro do widget específico
        widget.querySelectorAll("select").forEach(select => {
            if (!select.classList.contains("form-select")) {
                select.classList.add("form-select");
            }
        });

        widget.querySelectorAll("input[type='text']").forEach(input => {
            if (!input.classList.contains("form-control")) {
                input.classList.add("form-control");
            }
        });

        // Seleciona "Choose" e "Remove" usando as classes e substitui pelo ícone no widget específico
        const chooseLink = widget.querySelector(".selector-add");
        const removeLink = widget.querySelector(".selector-remove");
        const chooseAllLink = widget.querySelector(".selector-chooseall");
        const removeAllLink = widget.querySelector(".selector-clearall");
        const searchIcon = widget.querySelectorAll(".search-label-icon");
        
        if (chooseLink) {
            chooseLink.classList.remove("selector-add"); // Remove classe padrão
            chooseLink.innerHTML = '<i class="bi bi-arrow-right-circle arrow"></i>'; // seta para direita
        }

        if (removeLink) {
            removeLink.classList.remove("selector-remove"); // Remove classe padrão
            removeLink.innerHTML = '<i class="bi bi-arrow-left-circle arrow"></i>'; // seta para esquerda
        }

        if (chooseAllLink) {
            chooseAllLink.classList.remove("selector-chooseall"); // Remove classe padrão
            chooseAllLink.classList.add("custom-chooseall"); // Adiciona uma classe personalizada para estilo
            chooseAllLink.innerHTML = 'Choose All <i class="bi bi-arrow-right-circle large-icon"></i>'; // seta em círculo
        }
        if (removeAllLink) {
            removeAllLink.classList.remove("selector-clearall"); // Remove classe padrão
            removeAllLink.classList.add("custom-clearall");
            removeAllLink.innerHTML = '<i class="bi bi-arrow-left-circle"></i> Remove All';
        }

        if (searchIcon) {
          searchIcon.forEach(icon => {
              icon.classList.remove("search-label-icon");
              icon.parentElement.classList.add("label-large"); // Aplica a classe ao label que envolve o ícone
              icon.innerHTML = '<i class="bi bi-search arrow"></i>';
          });
      }
    }

    // Aplica o estilo em cada widget relacionado
    renderedWidgets.forEach(applyStyles);

    // Observa mudanças em cada widget e aplica estilos novamente, mas desativa após a aplicação inicial
    renderedWidgets.forEach(widget => {
        const observer = new MutationObserver(function(mutationsList, observer) {
            applyStyles(widget);
            observer.disconnect(); // Desativa o observer após a primeira aplicação
        });

        observer.observe(widget, { childList: true, subtree: true });
    });
  }
);
})()