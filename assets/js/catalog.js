(function () {
  "use strict";

  function normalize(value) {
    return String(value || "")
      .toLowerCase()
      .replace(/[^a-z0-9]+/g, " ")
      .trim();
  }

  document.addEventListener("DOMContentLoaded", function () {
    var searchInput = document.getElementById("game-search");
    var categoryFilter = document.getElementById("category-filter");
    var clearButton = document.getElementById("clear-filters");
    var randomButton = document.getElementById("random-game");
    var countNode = document.getElementById("result-count");
    var emptyState = document.getElementById("empty-state");
    var cards = Array.prototype.slice.call(document.querySelectorAll("[data-game-card]"));

    if (!searchInput || !categoryFilter || cards.length === 0) {
      return;
    }

    var params = new URLSearchParams(window.location.search);
    searchInput.value = params.get("q") || "";
    categoryFilter.value = params.get("type") || "";

    function visibleCards() {
      return cards.filter(function (card) {
        return !card.hidden;
      });
    }

    function updateUrl(query, category) {
      var nextParams = new URLSearchParams(window.location.search);
      if (query) {
        nextParams.set("q", query);
      } else {
        nextParams.delete("q");
      }
      if (category) {
        nextParams.set("type", category);
      } else {
        nextParams.delete("type");
      }
      var queryString = nextParams.toString();
      var nextUrl = window.location.pathname + (queryString ? "?" + queryString : "") + "#game-catalog";
      window.history.replaceState(null, "", nextUrl);
    }

    function applyFilters(syncUrl) {
      var rawQuery = searchInput.value.trim();
      var query = normalize(rawQuery);
      var category = categoryFilter.value;
      var count = 0;

      cards.forEach(function (card) {
        var haystack = normalize(card.getAttribute("data-search"));
        var cardCategory = card.getAttribute("data-category") || "";
        var matchesQuery = !query || haystack.indexOf(query) !== -1;
        var matchesCategory = !category || cardCategory === category;
        var show = matchesQuery && matchesCategory;
        card.hidden = !show;
        if (show) {
          count += 1;
        }
      });

      countNode.textContent = count + (count === 1 ? " game" : " games");
      emptyState.hidden = count !== 0;
      randomButton.disabled = count === 0;

      if (syncUrl !== false) {
        updateUrl(rawQuery, category);
      }
    }

    searchInput.addEventListener("input", function () {
      applyFilters(true);
    });

    categoryFilter.addEventListener("change", function () {
      applyFilters(true);
    });

    clearButton.addEventListener("click", function () {
      searchInput.value = "";
      categoryFilter.value = "";
      applyFilters(true);
      searchInput.focus();
    });

    randomButton.addEventListener("click", function () {
      var candidates = visibleCards();
      if (candidates.length === 0) {
        return;
      }
      var index = Math.floor(Math.random() * candidates.length);
      window.location.assign(candidates[index].href);
    });

    applyFilters(false);
  });
})();
