let currentIndex = 0;
const reviewsPerPage = 5;
const reviewsContainer = document.getElementById('reviews-container');

// Retrieve comments from JSON file
async function fetchReviews() {
    try {
        const response = await fetch('reviews.json'); // If there is a backend API you can write '/api/comments'
        const data = await response.json();
        displayReviews(data);
    } catch (error) {
        console.error('Veri yüklenemedi:', error);
    }
}

// Display comments in HTML
function displayReviews(reviews) {
    const reviewsToDisplay = reviews.slice(currentIndex, currentIndex + reviewsPerPage);

    reviewsToDisplay.forEach(review => {
        const reviewCard = document.createElement('div');
        reviewCard.className = 'review-card';
        reviewCard.innerHTML = `
            <h3>${review.name}</h3>
            <div class="date">${review.date}</div>
            <p>${review.comment}</p>
        `;
        reviewsContainer.appendChild(reviewCard);
    });

    currentIndex += reviewsPerPage;

    // If there are more comments, show upload button
    if (currentIndex < reviews.length) {
        document.getElementById('load-more').style.display = 'block';
    } else {
        document.getElementById('load-more').style.display = 'none';
    }
}

// Load more comments
document.getElementById('load-more').addEventListener('click', () => {
    fetchReviews();
});

// First pull the comments
fetchReviews();
