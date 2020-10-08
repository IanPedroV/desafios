package idwall.desafio.string;

public class IdwallFormatter implements StringFormatter {

    public IdwallFormatter(int lineCharLimit, boolean shouldJustify) {
        this.lineCharLimit = lineCharLimit;
        this.shouldJustify = shouldJustify;
    }

    public final int lineCharLimit;
    public final boolean shouldJustify;

    /**
     * {@inheritDoc}
     */
    @Override
    public String format(String text) {
        throw new UnsupportedOperationException();
    }


}
