// Enhanced Toast System - Bottom Right Position (NO BROWSER ALERTS)
class ToastManager {
    static show(type, title, message, duration = 5000) {
        const container = this.getOrCreateToastContainer();
        const template = document.getElementById('toast-template');

        if (!template) {
            console.error('Toast template not found');
            // NO BROWSER ALERTS - just log to console
            console.log(`[Custom Toast] ${title}: ${message}`);
            return;
        }

        const toast = template.content.cloneNode(true);
        const toastElement = toast.querySelector('.toast-item');
        const toastId = 'toast-' + Date.now() + '-' + Math.random().toString(36).substr(2, 9);
        toastElement.id = toastId;

        // Set toast type styles
        const typeStyles = {
            success: {
                bg: 'bg-white/95 border-l-green-500 text-green-800 shadow-lg',
                icon: `
                    <svg class="w-4 h-4 text-green-500" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
                    </svg>
                `
            },
            error: {
                bg: 'bg-white/95 border-l-red-500 text-red-800 shadow-lg',
                icon: `
                    <svg class="w-4 h-4 text-red-500" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd"/>
                    </svg>
                `
            },
            warning: {
                bg: 'bg-white/95 border-l-yellow-500 text-yellow-800 shadow-lg',
                icon: `
                    <svg class="w-4 h-4 text-yellow-500" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd"/>
                    </svg>
                `
            },
            info: {
                bg: 'bg-white/95 border-l-blue-500 text-blue-800 shadow-lg',
                icon: `
                    <svg class="w-4 h-4 text-blue-500" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd"/>
                    </svg>
                `
            }
        };

        const style = typeStyles[type] || typeStyles.info;

        toastElement.classList.add(...style.bg.split(' '));
        toastElement.querySelector('.toast-icon').innerHTML = style.icon;
        toastElement.querySelector('.toast-title').textContent = title;
        toastElement.querySelector('.toast-message').textContent = message;

        // Add to container (prepend to show newest at bottom)
        container.insertBefore(toast, container.firstChild);

        // Animate in
        requestAnimationFrame(() => {
            toastElement.classList.add('toast-enter');
            toastElement.classList.remove('opacity-0', 'translate-y-full', 'max-h-0', 'mb-0');
            toastElement.classList.add('opacity-100', 'translate-y-0', 'max-h-32', 'mb-3');
        });

        // Progress bar animation
        const progressBar = toastElement.querySelector('.toast-progress');
        if (progressBar) {
            progressBar.style.width = '100%';
            progressBar.style.transition = `width ${duration}ms linear`;
            setTimeout(() => {
                progressBar.style.width = '0%';
            }, 10);
        }

        // Auto remove
        const removeToast = () => {
            toastElement.classList.add('toast-exit');
            toastElement.classList.remove('opacity-100', 'translate-y-0', 'max-h-32', 'mb-3');
            toastElement.classList.add('opacity-0', 'translate-y-full', 'max-h-0', 'mb-0');

            setTimeout(() => {
                if (toastElement.parentNode) {
                    toastElement.parentNode.removeChild(toastElement);
                }
            }, 300);
        };

        // Close button
        const closeBtn = toastElement.querySelector('.toast-close');
        if (closeBtn) {
            closeBtn.addEventListener('click', (e) => {
                e.stopPropagation();
                removeToast();
            });
        }

        // Click to dismiss
        toastElement.addEventListener('click', removeToast);

        // Auto remove after duration
        const autoRemoveTimeout = setTimeout(removeToast, duration);

        // Pause on hover
        toastElement.addEventListener('mouseenter', () => {
            if (progressBar) {
                progressBar.style.transition = 'none';
                progressBar.style.width = progressBar.style.width;
            }
            clearTimeout(autoRemoveTimeout);
        });

        toastElement.addEventListener('mouseleave', () => {
            if (progressBar) {
                const remainingWidth = parseFloat(progressBar.style.width);
                const remainingTime = (remainingWidth / 100) * duration;
                progressBar.style.transition = `width ${remainingTime}ms linear`;
                progressBar.style.width = '0%';
            }
            setTimeout(removeToast, duration);
        });

        return toastId;
    }

    static getOrCreateToastContainer() {
        let container = document.getElementById('toast-container');
        if (!container) {
            container = document.createElement('div');
            container.id = 'toast-container';
            container.className = 'fixed bottom-4 right-4 z-50 flex flex-col gap-3 w-80 max-w-full';
            document.body.appendChild(container);
        }
        return container;
    }

    static productCreated(productName) {
        this.show('success', 'Product Created', `"${productName}" has been added successfully!`);
        this.dispatchProductUpdate();
    }

    static productUpdated(productName) {
        this.show('success', 'Product Updated', `"${productName}" has been updated successfully!`);
        this.dispatchProductUpdate();
    }

    static productDeleted(productName) {
        this.show('success', 'Product Deleted', `"${productName}" has been removed successfully!`);
        this.dispatchProductUpdate();
    }

    static loginSuccess(username) {
        this.show('success', 'Welcome Back!', `Hello ${username}, you're now logged in.`);
    }

    static logoutSuccess() {
        this.show('info', 'Goodbye!', 'You have been logged out successfully.');
    }

    static registerSuccess() {
        this.show('success', 'Welcome!', 'Your account has been created successfully!');
    }

    static error(title, message) {
        this.show('error', title, message, 7000);
    }

    static info(title, message) {
        this.show('info', title, message, 5000);
    }

    static warning(title, message) {
        this.show('warning', title, message, 6000);
    }

    static dispatchProductUpdate() {
        const event = new CustomEvent('productsUpdated', {
            detail: { timestamp: new Date().toISOString() }
        });
        document.dispatchEvent(event);
    }

    // Method to manually remove a toast by ID
    static removeToast(toastId) {
        const toast = document.getElementById(toastId);
        if (toast) {
            toast.classList.add('toast-exit');
            setTimeout(() => {
                if (toast.parentNode) {
                    toast.parentNode.removeChild(toast);
                }
            }, 300);
        }
    }

    // Method to clear all toasts
    static clearAll() {
        const container = this.getOrCreateToastContainer();
        const toasts = container.querySelectorAll('.toast-item');
        toasts.forEach(toast => {
            toast.classList.add('toast-exit');
            setTimeout(() => {
                if (toast.parentNode) {
                    toast.parentNode.removeChild(toast);
                }
            }, 300);
        });
    }
}

// Initialize toast system when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Create toast container if it doesn't exist
    ToastManager.getOrCreateToastContainer();

    // Check for stored messages in sessionStorage
    const storedToast = sessionStorage.getItem('pendingToast');
    if (storedToast) {
        try {
            const { type, title, message } = JSON.parse(storedToast);
            setTimeout(() => {
                ToastManager.show(type, title, message);
            }, 500);
            sessionStorage.removeItem('pendingToast');
        } catch (e) {
            console.error('Error parsing stored toast:', e);
        }
    }

    // Add keyboard shortcut to clear all toasts (Ctrl+Shift+T)
    document.addEventListener('keydown', function(e) {
        if (e.ctrlKey && e.shiftKey && e.key === 'T') {
            e.preventDefault();
            ToastManager.clearAll();
        }
    });
});