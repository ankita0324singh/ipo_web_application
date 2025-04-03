document.addEventListener("DOMContentLoaded", function() {
    const ipoListContainer = document.getElementById("ipo-list");

    // Replace with actual API URL
    fetch("https://your-backend-api.com/ipo-data")  
        .then(response => response.json())
        .then(data => {
            ipoListContainer.innerHTML = data.map(ipo => `
                <div class="col-md-4 mb-4">
                    <div class="card p-3">
                        <div class="text-center">
                            <img src="${ipo.logo}" alt="${ipo.company_name} Logo" class="company-logo">
                        </div>
                        <h5 class="text-center mt-2">${ipo.company_name}</h5>
                        <div class="ipo-details">
                            <p><strong>Price Band:</strong> ${ipo.price_band}</p>
                            <p><strong>Open Date:</strong> ${ipo.open_date}</p>
                            <p><strong>Close Date:</strong> ${ipo.close_date}</p>
                            <p><strong>Issue Size:</strong> ${ipo.issue_size}</p>
                            <p><strong>Issue Type:</strong> ${ipo.issue_type}</p>
                            <p><strong>Listing Date:</strong> ${ipo.listing_date}</p>
                            <p><strong>Status:</strong> ${ipo.status}</p>
                            <p><strong>IPO Price:</strong> ₹${ipo.ipo_price}</p>
                            <p><strong>Listing Price:</strong> ₹${ipo.listing_price}</p>
                            <p><strong>Listing Gain:</strong> ${ipo.listing_gain}%</p>
                            <p><strong>CMP:</strong> ₹${ipo.current_market_price}</p>
                            <p><strong>Current Return:</strong> ${ipo.current_return}%</p>
                            <p>
                                <a href="${ipo.rhp_pdf}" class="btn btn-primary btn-sm" target="_blank">RHP PDF</a>
                                <a href="${ipo.drhp_pdf}" class="btn btn-secondary btn-sm" target="_blank">DRHP PDF</a>
                            </p>
                        </div>
                    </div>
                </div>
            `).join('');
        })
        .catch(error => {
            console.error("Error fetching IPO data:", error);
            ipoListContainer.innerHTML = "<p class='text-danger'>Failed to load IPO data.</p>";
        });
});
